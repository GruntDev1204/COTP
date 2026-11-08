import random
from data.data import *

def ruleL4D2():
    output = (
        f"Rule of this game (L4D2): Người chơi làm theo mục tiêu, Zombie cố định luôn là tank, trong 1 khoảng thời gian và số bước di chuyển được giới hạn:\n\n"
        f"Map: {random.choice(mapsL4D2)} - Campaign của map sẽ được random (trừ map cuối)\n"
        f"Character : {random.choice(charactersL4D2)}\n"
        f"Player HP : {random.randint(1, 100):,}\n"
        + (
            f"Weapon : {random.choice(weaponsL4D2)} - ammo : {random.randint(1, 500)}\n"
            if random.randint(0, 1) == 1
            else "Weapon : None\n"
        )
        + f"Melee: {random.choice(meleeL4D2)}\n"
        f"Grenade : {random.choice(grenadesL4D2)} - quantity : {random.randint(0, 5)}\n"
        f"Pickups : {random.choice(pickupsL4D2)} - quantity : {random.randint(0, 5)}\n"
        f"Medicine : {random.choice(medicineL4D2)} - quantity : {random.randint(0, 5)}\n"
        f"First Aid Kits  : {random.randint(0, 3)}\n"   
        f"Tank Health : {random.randint(1000000000, 100000000000):,}\n"
        f"Common Infected : {random.randint(1, 100):,} zombies\n"
        f"Time limit: {random.randint(2, 5)} minutes\n"
        f"Step limit: {random.randint(100, 500)} steps\n"
        f"Player Rules : {random.choice(playerRulesL4D2)} - time limit: {random.randint(10, 60)} seconds\n"
        f"Objective : {random.choice(['escape', 'kill the tank', 'survive'])}\n"
    )
    return output

def dateAppOptions():
    output = (
        f"Chào mừng đến với ứng dụng tài xỉu xổ số hẹn hò `SIDA VKL QUỐC TẾ ${random.choice(companies)}`. \n\n"
        f"Reject Number of Profiles (số lượt phải quẹt trái): {random.randint(1,20):,} profiles\n"
        f"Like Number of Profiles (số lượt phải quẹt phải): {random.randint(1,20):,} profiles\n"
        f"Options: {random.choice(optionsDateApp)} \n"
    )
    return output
