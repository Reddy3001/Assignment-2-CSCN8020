#!/usr/bin/python3
import time
import gymnasium as gym


def describe_env(env):
    act = env.action_space
    obs = env.observation_space
    num_obs = getattr(obs, "n", None)
    num_act = getattr(act, "n", None)

    # Safely get reward_range even if wrapped by TimeLimit
    reward_range = getattr(env, "reward_range", None)
    if reward_range is None and hasattr(env, "unwrapped"):
        reward_range = getattr(env.unwrapped, "reward_range", None)

    # Final fallback for Taxi-v3
    if reward_range is None:
        reward_range = (-10, 20)

    action_desc = {
        0: "Move south (down)",
        1: "Move north (up)",
        2: "Move east (right)",
        3: "Move west (left)",
        4: "Pick up passenger",
        5: "Drop off passenger",
    }

    print("Observation space:", obs)
    if num_obs is not None:
        print("Number of states:", num_obs)
    print("Action space:", act)
    if num_act is not None:
        print("Number of actions:", num_act)
    print("Reward range:", reward_range)
    print("Action descriptions:", action_desc)
    return {
        "obs_space": str(obs),
        "num_states": num_obs,
        "action_space": str(act),
        "num_actions": num_act,
        "reward_range": reward_range,
        "action_desc": action_desc,
    }
