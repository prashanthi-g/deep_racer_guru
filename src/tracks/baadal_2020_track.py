from src.tracks.track import Track



# Other people might want to change/personalize these values

PRIVATE_DESCRIPTION = "Baadal - April 2020"
#PRIVATE_SECTION_DIVIDERS = [8,11,17,23,30,34,40,43,44,46,50,56,58,63,68,74,76,90,95,98,102,107,114,120,125,129,133,139,144,154,158]
PRIVATE_SECTION_DIVIDERS = [17,23,28,33, 90, 95, 101, 120, 125, 126, 132]


class Baadal2020Track(Track):
    def __init__(self):
        super().__init__()

        # Details of the track as it appears on the training UI
        self.ui_name = "Baadal Track"

        self.ui_description = "Baadal is the Hindi word for cloud. The Baadal track combines long arching straightaways perfect for passing opportunities coupled with tight windings corners."
        self.ui_length_in_m = 39.0 # metres
        self.ui_width_in_cm = 107 # centimetres
        self.ui_difficulty = "*NONE*"

        # Other bits of basic info
        self.private_description = PRIVATE_DESCRIPTION
        self.world_name = "AmericasGenerated..."

        # Divide track into sections
        self.track_section_dividers = PRIVATE_SECTION_DIVIDERS

        # Now the track definition info - as given to the reward function
        self.track_width = 1.07
        self.track_waypoints = [
            [-5.66000294685364, 3.958880424499509],
            [-5.7570354938507045, 3.8440994024276773],
            [-5.85366678237915, 3.728980541229248],
            [-5.9498066902160645, 3.6134519577026367],
            [-6.045382499694827, 3.4974545240402195],
            [-6.140244483947754, 3.3808740377426147],
            [-6.23428201675415, 3.263625979423523],
            [-6.327301025390625, 3.145568013191223],
            [-6.419062852859497, 3.026531457901001],
            [-6.509337902069092, 2.9063609838485718],
            [-6.597744464874268, 2.784808039665222],
            [-6.683832406997681, 2.6616060733795166],
            [-6.767106056213379, 2.5364795923233032],
            [-6.846842050552368, 2.409065008163452],
            [-6.922170162200928, 2.278998017311096],
            [-6.992099046707153, 2.1459575295448303],
            [-7.055515289306641, 2.0096899271011353],
            [-7.111108064651489, 1.8700449466705322],
            [-7.1574482917785645, 1.7270634770393372],
            [-7.193072557449341, 1.5810449719429016],
            [-7.216602563858032, 1.4326010346412659],
            [-7.226910352706909, 1.282662034034729],
            [-7.223280429840088, 1.1324154734611511],
            [-7.205502510070801, 0.9831812381744385],
            [-7.173877477645874, 0.8362545371055603],
            [-7.12910008430481, 0.6927842497825623],
            [-7.072093963623047, 0.5537201464176178],
            [-7.003833532333374, 0.4198261573910713],
            [-6.925275087356567, 0.2917060856707394],
            [-6.837337017059326, 0.1698335036635399],
            [-6.740900278091431, 0.05456584692001343],
            [-6.636804103851318, -0.05384095013141632],
            [-6.525861978530884, -0.15522754937410355],
            [-6.408857583999634, -0.24954623728990555],
            [-6.286554336547852, -0.33689118549227715],
            [-6.159768104553223, -0.41759130731225014],
            [-6.029304027557373, -0.49220180232077837],
            [-5.895843029022217, -0.5613089203834534],
            [-5.76002049446106, -0.6256571263074875],
            [-5.622736930847168, -0.6868360713124275],
            [-5.485501050949097, -0.7481200397014618],
            [-5.3488609790802, -0.8107256591320038],
            [-5.211751937866211, -0.8722924590110779],
            [-5.073456287384033, -0.9311444908380508],
            [-4.933642864227295, -0.9862889796495438],
            [-4.792094469070435, -1.036812037229538],
            [-4.648606538772583, -1.0815193057060242],
            [-4.503013372421265, -1.1188102066516876],
            [-4.355359077453613, -1.1467895805835724],
            [-4.206019878387451, -1.1635716259479523],
            [-4.055790424346924, -1.1672404110431671],
            [-3.9059489965438843, -1.1560732126235962],
            [-3.758147954940796, -1.128980278968811],
            [-3.6141995191574097, -1.0859194993972778],
            [-3.4754245281219482, -1.0282890498638153],
            [-3.3421205282211304, -0.9589154720306396],
            [-3.3421205282211304, -0.9589154720306396],
            [-3.2135485410690308, -0.8810970187187195],
            [-3.088540554046631, -0.7976623773574829],
            [-2.965657591819763, -0.7111210376024246],
            [-2.843257427215576, -0.6238968744874],
            [-2.7195885181427, -0.5384870730340481],
            [-2.59333598613739, -0.4569522733800113],
            [-2.4632264375686646, -0.38176506757736206],
            [-2.3256880044937134, -0.32156120985746384],
            [-2.179579973220825, -0.28706925362348557],
            [-2.0299980640411377, -0.273239403963089],
            [-1.8798149824142456, -0.27655796706676483],
            [-1.7314364910125732, -0.2997157424688339],
            [-1.5887594819068909, -0.34645455330610275],
            [-1.4560675024986267, -0.41673270240426064],
            [-1.3352516293525696, -0.5059823356568813],
            [-1.2248230278491974, -0.6078851073980331],
            [-1.1215990483760834, -0.7171147763729095],
            [-1.0225889980793, -0.8301890939474106],
            [-0.9255050122737885, -0.9449261128902435],
            [-0.8285874128341675, -1.0598032176494598],
            [-0.7303529530763626, -1.1735552251338959],
            [-0.6294289901852608, -1.2849246263504028],
            [-0.5243336632847786, -1.3923614621162415],
            [-0.41355532407760587, -1.4939134716987612],
            [-0.2957906424999237, -1.5872640013694763],
            [-0.17018990218639374, -1.6697425246238708],
            [-0.03682074695825577, -1.738929569721222],
            [0.10313616693019867, -1.7936034798622131],
            [0.2477007545530796, -1.8346160650253296],
            [0.3949059396982193, -1.864874541759491],
            [0.5434390008449554, -1.8878219723701477],
            [0.6926046311855316, -1.906228482723236],
            [0.8420867025852192, -1.9218769669532774],
            [0.9917286932468414, -1.9359135627746582],
            [1.141459047794342, -1.9489820003509521],
            [1.2912429571151733, -1.9614179730415344],
            [1.4410669803619394, -1.9733539819717407],
            [1.590930461883545, -1.9847924709320068],
            [1.7408375144004822, -1.9956409931182861],
            [1.8907954692840576, -2.0057650208473206],
            [2.0408074855804443, -2.015045464038849],
            [2.190874457359314, -2.0233999490737915],
            [2.3409935235977173, -2.0307684540748596],
            [2.4911584854125977, -2.037106990814209],
            [2.6413655281066886, -2.042383551597595],
            [2.7916065454483032, -2.0465720295906067],
            [2.9418740272521973, -2.049651026725769],
            [3.09216046333313, -2.051601529121399],
            [3.2424575090408325, -2.0524014234542847],
            [3.3927565813064575, -2.052029013633728],
            [3.543047547340394, -2.050457537174225],
            [3.6933209896087646, -2.047650456428528],
            [3.843564510345459, -2.0435635447502136],
            [3.9937654733657837, -2.038130462169647],
            [4.14390754699707, -2.031254470348358],
            [4.293969392776489, -2.0228084325790405],
            [4.4439239501953125, -2.012627959251404],
            [4.593732833862305, -2.000502049922943],
            [4.743346929550171, -1.9861674904823303],
            [4.892695903778076, -1.9693000316619873],
            [5.041685104370117, -1.9495030641555786],
            [5.190182447433472, -1.926309049129486],
            [5.338014125823975, -1.899193525314331],
            [5.484953880310059, -1.8676044344902039],
            [5.630725145339966, -1.831009030342102],
            [5.774989366531372, -1.788862943649292],
            [5.917303562164307, -1.740548014640808],
            [6.057107925415039, -1.685393512248993],
            [6.193664073944092, -1.6226370334625244],
            [6.326013803482054, -1.551440477371217],
            [6.4528703689575195, -1.4708830118179321],
            [6.572597980499268, -1.3800653219223022],
            [6.683197021484376, -1.278355926275252],
            [6.782935857772827, -1.1659643352031708],
            [6.870671510696411, -1.043982058763504],
            [6.94607400894165, -0.913995623588562],
            [7.009504556655884, -0.777768462896347],
            [7.061788320541382, -0.6368705928325653],
            [7.104021072387695, -0.49264395236968994],
            [7.137322902679443, -0.34608865529298605],
            [7.16273045539856, -0.197959803044796],
            [7.180895090103149, -0.04877026006579399],
            [7.192022800445557, 0.10111184790730476],
            [7.1959075927734375, 0.25135190784931183],
            [7.191936492919922, 0.4015893936157207],
            [7.179050445556641, 0.5513217002153397],
            [7.155781030654907, 0.6997877955436707],
            [7.120370864868164, 0.845827043056488],
            [7.071115016937255, 0.9877869188785569],
            [7.007126569747925, 1.1237331628799438],
            [6.928703069686889, 1.2519059181213392],
            [6.837066888809204, 1.370985507965088],
            [6.7338244915008545, 1.4801740050315857],
            [6.620632886886597, 1.579014003276825],
            [6.4989495277404785, 1.6671879887580872],
            [6.369964361190796, 1.7443130612373352],
            [6.234682559967039, 1.8097364306449897],
            [6.094013452529907, 1.8625964522361755],
            [5.949002504348755, 1.9020445346832275],
            [5.80089807510376, 1.927435040473938],
            [5.651031017303465, 1.9384949803352356],
            [5.5007874965667725, 1.9354159832000732],
            [5.351424932479858, 1.9189165234565735],
            [5.203908443450928, 1.8902084231376648],
            [5.058817148208621, 1.8510524630546576],
            [4.916203022003174, 1.8036289811134338],
            [4.77564549446106, 1.7504124641418457],
            [4.636264801025391, 1.694172441959381],
            [4.496432542800903, 1.6390774846076965],
            [4.35332989692688, 1.5933269262313843],
            [4.20458459854126, 1.5746829509735107],
            [4.049918055534363, 1.601656436920166],
            [3.9198169708251953, 1.6621540188789368],
            [3.788592576980591, 1.735415518283844],
            [3.6582034826278687, 1.810169517993927],
            [3.5249539613723755, 1.879661500453949],
            [3.386465549468994, 1.9379565119743347],
            [3.2422115802764893, 1.9799144864082336],
            [3.0937575101852417, 2.002890944480896],
            [2.9435755014419556, 2.007458508014679],
            [2.7936575412750244, 1.9971559643745422],
            [2.644674062728882, 1.9773675203323364],
            [2.4961490631103516, 1.9543344974517822],
            [2.3470449447631836, 1.9355109333992004],
            [2.1969469785690308, 1.9284019470214844],
            [2.0471014976501465, 1.9390785098075867],
            [1.9001749753952026, 1.9704304933547974],
            [1.7589374780654907, 2.021634042263031],
            [1.6246790289878845, 2.089140474796295],
            [1.4970124959945679, 2.168420433998108],
            [1.3744670152664213, 2.2554309368133523],
            [1.2550445199012756, 2.3466904759407043],
            [1.136623501777649, 2.4392449855804443],
            [1.0175322592258453, 2.5309349298477173],
            [0.8965888321399689, 2.62016499042511],
            [0.7730114161968201, 2.7057089805603045],
            [0.646395280957222, 2.786687970161438],
            [0.516713559627533, 2.862656593322754],
            [0.38432036340236664, 2.9337960481643677],
            [0.24994239117950662, 3.0011165142059304],
            [0.11478725075721741, 3.0668665170669556],
            [-0.019242696464061737, 3.134871482849121],
            [-0.14943695068359156, 3.209935903549193],
            [-0.2720812577754259, 3.296726942062378],
            [-0.38277214812114835, 3.3982945680618286],
            [-0.47733404859900325, 3.5150060653686506],
            [-0.5537961088120937, 3.6443090438842773],
            [-0.6129774041473877, 3.7824189662933385],
            [-0.6577053144574165, 3.925875663757324],
            [-0.6913427039980888, 4.07235062122345],
            [-0.7168591022491446, 4.220460653305048],
            [-0.736379757523537, 4.369482517242435],
            [-0.7515415772795677, 4.519012928009033],
            [-0.7636354416608809, 4.6688239574432355],
            [-0.7737331688404083, 4.818783521652222],
            [-0.7827220559120178, 4.968812942504883],
            [-0.7912855893373492, 5.118867874145511],
            [-0.7999028712511063, 5.268920660018921],
            [-0.8094909340143204, 5.418912887573242],
            [-0.8219924718141556, 5.5686869621276855],
            [-0.8406123220920559, 5.717813491821286],
            [-0.8697943985462189, 5.865213632583618],
            [-0.9145664423704163, 6.008611679077152],
            [-0.9786119759082794, 6.144468545913696],
            [-1.0616509914398193, 6.2696332931518555],
            [-1.160482794046402, 6.382781982421875],
            [-1.2714843153953552, 6.484057426452637],
            [-1.391730010509491, 6.574174165725708],
            [-1.519204497337338, 6.653758287429808],
            [-1.6525489687919617, 6.723059892654419],
            [-1.7908880114555359, 6.781764507293701],
            [-1.9335185289382935, 6.829078912734985],
            [-2.0797035098075867, 6.863890647888184],
            [-2.228494524955753, 6.884876012802124],
            [-2.3786330223083496, 6.890727519989014],
            [-2.528536081314087, 6.880491018295288],
            [-2.676444411277771, 6.854072093963623],
            [-2.8209365606307935, 6.812851190567018],
            [-2.961097002029419, 6.75869345664978],
            [-3.0957679748535156, 6.692063331604004],
            [-3.2232725620269775, 6.612581491470337],
            [-3.342753529548645, 6.521458625793457],
            [-3.455515503883362, 6.422109603881836],
            [-3.5637189149856567, 6.317797899246216],
            [-3.669121026992798, 6.210652828216553],
            [-3.7727506160736084, 6.101792097091675],
            [-3.87520492076874, 5.9918239116668675],
            [-3.9768350124359104, 5.881093978881839],
            [-4.077861428260806, 5.769812345504758],
            [-4.1784268617630005, 5.658114910125732],
            [-4.278627514839172, 5.546089172363281],
            [-4.37852597236633, 5.433794021606449],
            [-4.478174924850464, 5.321277618408203],
            [-4.577608585357666, 5.208571195602417],
            [-4.676850557327273, 5.095695495605466],
            [-4.775922060012817, 4.982670545578003],
            [-4.874833583831787, 4.869504928588867],
            [-4.973595142364502, 4.756208896636963],
            [-5.07220792770386, 4.642782926559446],
            [-5.1706695556640625, 4.529226541519165],
            [-5.26896333694458, 4.415524482727051],
            [-5.367077112197876, 4.301666617393494],
            [-5.464974880218503, 4.187623381614689],
            [-5.562634944915774, 4.073376059532163],
            [-5.66000294685364, 3.958880424499509]
        ]


