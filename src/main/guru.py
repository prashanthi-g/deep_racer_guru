import tkinter as tk
from os import chdir

import src.secret_sauce.glue.glue as ss
import src.configuration.personal_configuration as config


from src.analyze.analyze_convergence import AnalyzeConvergence
from src.analyze.analyze_route import AnalyzeRoute
from src.episode.episode_filter import EpisodeFilter
from src.graphics.track_graphics import TrackGraphics
from src.log.log import Log
from src.main.view_manager import ViewManager
from src.tracks.tracks import get_all_tracks
from src.ui.menu_bar import MenuBar
from src.ui.status_frame import StatusFrame
from src.action_space.action_space_filter import ActionSpaceFilter



class MainApp(tk.Frame):
    def __init__(self, root):
        #
        # Basic frame initialization
        #

        super().__init__(root)

        #
        # Initialise all internal settings not related to UI components
        #

        self.tracks = get_all_tracks()
        self.current_track = self.tracks["FS_June2020"]

        self.log = None
        self.filtered_episodes = None

        self.episode_filter = EpisodeFilter()
        self.view_manager = ViewManager()
        self.action_space_filter = ActionSpaceFilter()


        #
        # Go to the correct directory where the log files are located, ready to load or save them there
        #

        chdir(config.LOG_DIRECTORY)

        #
        # Create the high level UI components (the canvas, control frame and status frame)
        #

        self.status_frame = StatusFrame(self)

        self.track_canvas = tk.Canvas(self, bg="black", width=700, height=500)
        self.track_canvas.bind("<Configure>", self.redraw)
        self.track_canvas.bind("<Button-1>", self.left_button_pressed_on_track_canvas)
        self.track_canvas.bind("<Left>", self.left_or_down_key_pressed_on_track_canvas)
        self.track_canvas.bind("<Up>", self.right_or_up_key_pressed_on_track_canvas)
        self.track_canvas.bind("<Right>", self.right_or_up_key_pressed_on_track_canvas)
        self.track_canvas.bind("<Down>", self.left_or_down_key_pressed_on_track_canvas)

        self.control_frame = tk.Frame(root)

        #
        # Create the various "analyzers" and let them take control of the contents of the high level UI components
        #

        self.track_graphics = TrackGraphics(self.track_canvas)
        self.analyze_route = AnalyzeRoute(self.redraw, self.track_graphics, self.control_frame)
        self.analyze_convergence = AnalyzeConvergence(self.redraw, self.track_graphics, self.control_frame)

        self.analyzer = self.analyze_route
        self.all_analyzers = [self.analyze_route, self.analyze_convergence]
        self.analyzer.set_track(self.current_track)
        self.analyzer.take_control()

        if ss.SHOW_SS:
            self.secret_analyzers = ss.get_secret_analyzers(self.redraw, self.track_graphics, self.control_frame)
        else:
            self.secret_analyzers = None

        #
        # Define the layout of the high level UI components
        #

        self.status_frame.pack(side=tk.BOTTOM)
        self.track_canvas.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.control_frame.pack(side=tk.RIGHT)
        self.pack(fill=tk.BOTH, expand=True)

        #
        # Configure the rest of the application window and then make it appear
        #

        self.master.title("Deep Racer Guru")
        self.menu_bar = MenuBar(root, self, False)

        #
        # All done, so display main window now
        #

        self.update()

    def menu_callback_switch_track(self, new_track):
        self.log = None
        self.filtered_episodes = None

        self.status_frame.reset()

        self.current_track = new_track

        for v in self.all_analyzers:
            v.set_track(new_track)

        self.analyzer.set_track(self.current_track)
        self.analyzer.set_filtered_episodes(self.filtered_episodes)

        self.redraw()

    def switch_analyzer(self, new_analyzer):
        self.analyzer = new_analyzer
        self.analyzer.set_track(self.current_track)
        self.analyzer.set_filtered_episodes(self.filtered_episodes)
        self.analyzer.take_control()

        self.redraw()

    def menu_callback_analyze_convergence(self):
        self.switch_analyzer(self.analyze_convergence)

    def menu_callback_analyze_route(self):
        self.switch_analyzer(self.analyze_route)

    def callback_open_this_file(self, file_name):
        # print("Loading ...", file_name)

        redraw_menu_afterwards = not self.log

        self.visitor_map = None

        self.log = Log()
        self.log.load_all(file_name)

        # Commented out now for public usage
        # self.log.log_meta.display_for_debug()
        # print("Loaded", file_name)

        self.status_frame.change_model_name(self.log.log_meta.model_name)
        self.apply_new_action_space()

        self.episode_filter.set_all_episodes(self.log.episodes)
        self.reapply_episode_filter()

        if redraw_menu_afterwards:
            self.menu_bar = MenuBar(root, self, True)
            self.update()

    def apply_new_action_space(self):
        self.action_space_filter.set_new_action_space(self.log.log_meta.action_space)
        for v in self.all_analyzers:
            v.set_action_space(self.log.log_meta.action_space)
            v.set_action_space_filter(self.action_space_filter)

    def reapply_action_space_filter(self):
        for v in self.all_analyzers:
            v.set_action_space_filter(self.action_space_filter)
        self.redraw()

    def reapply_episode_filter(self):
        self.filtered_episodes = self.episode_filter.get_filtered_episodes()

        for v in self.all_analyzers:
            v.set_filtered_episodes(self.filtered_episodes)

        self.status_frame.change_episodes(len(self.log.episodes), len(self.filtered_episodes))

        self.analyzer.set_filtered_episodes(self.filtered_episodes)

        self.redraw()

    def redraw(self, event=None):

        self.view_manager.redraw(self.current_track, self.track_graphics, self.analyzer)

    def left_button_pressed_on_track_canvas(self, event):
        track_point = self.track_graphics.get_real_point_for_widget_location(event.x, event.y)
        self.analyzer.left_button_pressed(track_point)
        self.track_canvas.focus_set() # Set focus so we will now receive keyboard events too

    def right_or_up_key_pressed_on_track_canvas(self, event):
        track_point = self.track_graphics.get_real_point_for_widget_location(event.x, event.y)
        self.analyzer.go_forwards(track_point)

    def left_or_down_key_pressed_on_track_canvas(self, event):
        track_point = self.track_graphics.get_real_point_for_widget_location(event.x, event.y)
        self.analyzer.go_backwards(track_point)

    def menu_callback_episodes_all(self):
        self.episode_filter.reset()
        self.reapply_episode_filter()

    def menu_callback_episodes_all_from_start(self):
        self.episode_filter.reset()
        self.episode_filter.set_filter_from_start_line(True)
        self.reapply_episode_filter()

    def menu_callback_episodes_complete_laps(self):
        self.episode_filter.reset()
        self.episode_filter.set_filter_complete_laps(True)
        self.reapply_episode_filter()

    def menu_callback_episodes_fast_laps(self):
        es = self.log.log_meta.episode_stats
        target_steps = round((es.average_steps + es.best_steps) / 2)

        self.episode_filter.reset()
        self.episode_filter.set_filter_complete_laps(True)
        self.episode_filter.set_filter_max_steps(target_steps)
        self.reapply_episode_filter()

    def menu_callback_episodes_complete_laps_from_start(self):
        self.episode_filter.reset()
        self.episode_filter.set_filter_complete_laps(True)
        self.episode_filter.set_filter_from_start_line(True)
        self.reapply_episode_filter()

    def menu_callback_episodes_min_percent_10(self):
        self.episode_filter.reset()
        self.episode_filter.set_filter_min_percent(10)
        self.reapply_episode_filter()

    def menu_callback_episodes_min_percent_25(self):
        self.episode_filter.reset()
        self.episode_filter.set_filter_min_percent(25)
        self.reapply_episode_filter()

    def menu_callback_episodes_min_percent_33(self):
        self.episode_filter.reset()
        self.episode_filter.set_filter_min_percent(33)
        self.reapply_episode_filter()

    def menu_callback_episodes_min_percent_50(self):
        self.episode_filter.reset()
        self.episode_filter.set_filter_min_percent(50)
        self.reapply_episode_filter()

    def menu_callback_actions_all(self):
        self.action_space_filter.set_filter_all()
        self.reapply_action_space_filter()

    def menu_callback_actions_high_speed(self):
        self.action_space_filter.set_filter_high_speed()
        self.reapply_action_space_filter()

    def menu_callback_actions_medium_speed(self):
        self.action_space_filter.set_filter_medium_speed()
        self.reapply_action_space_filter()

    def menu_callback_actions_low_speed(self):
        self.action_space_filter.set_filter_low_speed()
        self.reapply_action_space_filter()

    def menu_callback_actions_straight(self):
        self.action_space_filter.set_filter_straight()
        self.reapply_action_space_filter()

    def menu_callback_grid_front(self):
        self.view_manager.set_grid_front()
        self.redraw()

    def menu_callback_grid_back(self):
        self.view_manager.set_grid_back()
        self.redraw()

    def menu_callback_grid_off(self):
        self.view_manager.set_grid_off()
        self.redraw()

    def menu_callback_track_front(self):
        self.view_manager.set_track_front()
        self.redraw()

    def menu_callback_track_back(self):
        self.view_manager.set_track_back()
        self.redraw()

    def menu_callback_track_grey(self):
        self.view_manager.set_track_colour_grey()
        self.redraw()

    def menu_callback_track_blue(self):
        self.view_manager.set_track_colour_blue()
        self.redraw()

    def menu_callback_waypoints_large(self):
        self.view_manager.set_waypoint_sizes_large()
        self.redraw()

    def menu_callback_waypoints_small(self):
        self.view_manager.set_waypoint_sizes_small()
        self.redraw()

    def menu_callback_waypoints_micro(self):
        self.view_manager.set_waypoint_sizes_micro()
        self.redraw()

    def menu_callback_waypoints_off(self):
        self.view_manager.set_waypoints_off()
        self.redraw()

    def menu_callback_analyze_front(self):
        self.view_manager.set_analyze_front()
        self.redraw()

    def menu_callback_analyze_back(self):
        self.view_manager.set_analyze_back()
        self.redraw()




root = tk.Tk()
app = MainApp(root)
app.mainloop()