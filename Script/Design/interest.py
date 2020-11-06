import random
import numpy
from Script.Core import cache_contorl, constant
from Script.Config import game_config


def init_character_interest():
    """
    初始化全部角色兴趣/精力/天赋数值分配
    """
    interest_list = []
    language_skills = game_config.config_language.keys()
    language_average = 100 / len(language_skills)
    knowledge_skills = game_config.config_knowledge.keys()
    knowledge_average = 100 / len(knowledge_skills)
    for character in cache_contorl.character_data:
        now_knowledge_value_max = 100
        now_language_value_max = 100
        numpy.random.shuffle(knowledge_skills)
        numpy.random.shuffle(language_skills)
        for knowledge in knowledge_skills:
            if knowledge != knowledge_list[-1]:
                now_interest_average = now_knowledge_value_max / len(now_interest_list)
                now_inter_value = now_interest_average * random.uniform(0.75, 1.25)
                now_knowledge_value_max -= now_inter_value
                cache_contorl.character_data[character].knowledge_interest[interest] = (
                    now_inter_value / interest_average
                )
            else:
                cache_contorl.character_data[character].knowledge_interest[interest] = now_knowledge_value_max
        for language in language_skills:
            if language != language_list[-1]:
                now_interest_average = now_language_value_max / len(now_interest_list)
                now_inter_value = now_interest_average * random.uniform(0.75, 1.25)
                now_language_value_max -= now_inter_value
                cache_contorl.character_data[character].language_interest[interest] = (
                    now_inter_value / interest_average
                )
            else:
                cache_contorl.character_data[character].language_interest[interest] = now_language_value_max
