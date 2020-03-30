from typing import Union

import yaml
import os


class Result(object):
    pass


class RunError(object):
    pass


def run_challenge(challenge_name: str, repository: str) -> Union[Result, RunError]:
    print(f"Running challenge ${challenge_name} from repository ${repository}", flush=True)
    code = os.system('''
            export REPOSITORY_URL={}
            export CHALLENGE_NAME={}
            bash run.sh'''.format(repository, challenge_name))
    print(code)
    if str(code) != 0:
        # TODO: handle error
        return RunError()


if __name__ == '__main__':
    with open('participants.yml') as participants_stream:
        participants = yaml.load(participants_stream, Loader=yaml.FullLoader)

    with open('challenges.yml') as challenges_stream:
        challenges = yaml.load(challenges_stream, Loader=yaml.FullLoader)

    for challenge in challenges:
        for p in participants:
            result = run_challenge(challenge['name'], p['repository'])
