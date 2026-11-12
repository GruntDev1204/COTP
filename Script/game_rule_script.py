import random
from data.data import *
from Script.common_script import generateANumber

def ruleL4D2():
    output = (
        f"Rule of this game (L4D2): Người chơi làm theo mục tiêu, Zombie cố định luôn là tank, trong 1 khoảng thời gian và số bước di chuyển được giới hạn:\n\n"
        f"Map: {random.choice(mapsL4D2)} - Campaign của map sẽ được random (trừ map cuối)\n"
        f"Character : {random.choice(charactersL4D2)}\n"
        f"Player HP : {generateANumber(1, 100, includeType=False)}\n"
        + (
            f"Weapon : {random.choice(weaponsL4D2)} - ammo : {generateANumber(1, 500, includeType=False)}\n"
            if random.choice((True, False))
            else "Weapon : None\n"
        )
        + f"Melee: {random.choice(meleeL4D2)}\n"
        f"Grenade : {random.choice(grenadesL4D2)} - quantity : {generateANumber(0, 5, includeType=False)}\n"
        f"Pickups : {random.choice(pickupsL4D2)} - quantity : {generateANumber(0, 5, includeType=False)}\n"
        f"Medicine : {random.choice(medicineL4D2)} - quantity : {generateANumber(0, 5, includeType=False)}\n"
        f"First Aid Kits  : {generateANumber(0, 3, includeType=False)}\n"   
        f"Tank Health : {generateANumber(1000000000, 100000000000, includeType=False)}\n"
        f"Common Infected : {generateANumber(1, 100, includeType=False)} zombies\n"
        f"Time limit: {generateANumber(2, 5, includeType=False)} minutes\n"
        f"Step limit: {generateANumber(100, 500, includeType=False)} steps\n"
        f"Player Rules : {random.choice(playerRulesL4D2)} - time limit: {generateANumber(10, 60, includeType=False)} seconds\n"
        f"Objective : {random.choice(['escape', 'kill the tank', 'survive'])}\n"
    )
    return output

def dateAppOptions():
    output = (
        f"Chào mừng đến với ứng dụng tài xỉu xổ số hẹn hò `SIDA VKL QUỐC TẾ ${random.choice(companies)}`. \n\n"
        f"Reject Number of Profiles (số lượt phải quẹt trái): {generateANumber(1, 20, includeType=False)} profiles\n"
        f"Like Number of Profiles (số lượt phải quẹt phải): {generateANumber(1, 20, includeType=False)} profiles\n"
        f"Options: {random.choice(optionsDateApp)} \n"
    )
    return output
