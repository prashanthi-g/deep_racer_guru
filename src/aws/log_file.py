import src.configuration.personal_configuration as config
import boto3

LOG_LIMIT = 5000


def fetch_log_file(stream_name, log_group_name, file_name):
    aws_session = boto3.Session(profile_name=config.AWS_PROFILE_NAME)

    logs = aws_session.client('logs')

    response = logs.get_log_events(
        logGroupName=log_group_name,
        logStreamName=stream_name,
        startFromHead=True,
        limit=LOG_LIMIT
    )
    events = response['events']

    file = open(file_name, "w")

    while len(events) > 0:
        # print("Got", len(events), "events...")
        for e in events:
            file.write(e['message'] + '\n')

        response = logs.get_log_events(
            logGroupName=log_group_name,
            logStreamName=stream_name,
            startFromHead=True,
            nextToken=response['nextForwardToken'],
            limit=LOG_LIMIT
        )
        events = response['events']

    file.close()
