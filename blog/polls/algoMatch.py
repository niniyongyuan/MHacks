# Matching algorithm to determine teammate compatibility percentage

# Some slight syntax/variable modifications may need to be made to accommodate
# the fact that the function inputs come from SQL data

# Functions are algorithmically structured already here.

import math
import random

def genderMatch(genderA, genderB, teammateGenderA, teammateGenderB):
    if (genderB == teammateGenderA and genderA == teammateGenderB):
        return 100.0
    if (teammateGenderA == "No Preference" and teammateGenderB == "No Preference"):
        return 75.0
    if (teammateGenderA == "No Preference" and teammateGenderB != "No Preference"):
        if (genderA == teammateGenderB):
            return 100.0
        else:
            return 50.0
    if (teammateGenderB == "No Preference" and teammateGenderA != "No Preference"):
        if (genderB == teammateGenderA):
            return 100.0
        else:
            return 50.0
    if (genderB == teammateGenderA and genderA != teammateGenderB or
        genderB != teammateGenderA and genderA == teammateGenderB):
        return 50.0
    if (genderB != teammateGenderA and genderA != teammateGenderB):
        return 0.0

def schoolMatch(schoolA, schoolB):
    if (schoolA == schoolB):
        return 100.0
    return 0.0

def ageMatch(yearA, yearB):
    yearNums = {"Undergraduate-Freshman": 1, "Undergraduate-Sophomore": 2,
                "Undergraduate-Junior": 3, "Undergraduate-Senior": 4,
                "Masters": 4, "Doctoral": 5, "Other": random.randint(0, 6),
                "High School": 0}
    maxDiff = 48 # 8 possible years * 6 max difference
    diff = abs(yearNums[yearA]-yearNums[yearB])
    return 100.0*(1.0-float(diff)/maxDiff)

# takes in dictionaries of skills of person A and person B
# returns match rating difference
def skillMatch(skillsA, skillsB):
    maxDifference = 35 # 7 main/top skills * 5 max rating difference
    diffPython = abs(skillsA["Python"]-skillsB["Python"])
    diffJava = abs(skillsA["Java"]-skillsB["Java"])
    diffC = abs(skillsA["C"]-skillsB["C"])
    diffRuby = abs(skillsA["Ruby"]-skillsB["Ruby"])
    diffHTML = abs(skillsA["HTML"]-skillsB["HTML"])
    diffCSS = abs(skillsA["CSS"]-skillsB["CSS"])
    diffJS = abs(skillsA["JavaScript"]-skillsB["JavaScript"])
    ratingDiff = diffPython + diffJava + diffC + diffRuby + diffHTML + diffCSS + diffJS
    initialMatch = 100.0*(1.0-float(ratingDiff)/maxDifference)
    otherSkillsA = skillsA["Other Skills"]
    otherSkillsB = skillsB["Other Skills"]
    if (otherSkillsA == [] or otherSkillsB == []): # no misc skills in common
        return initialMatch
    commonMiscSkills = list(set(otherSkillsA) & set(otherSkillsB))
    numComm = len(commonMiscSkills)
    return 100.0*float(maxDifference-ratingDiff+5*numComm)/(maxDifference+5*numComm)

# Compare compatibility based on app preferences
def appPref(prefA1, prefA2, prefB1, prefB2):
    if (prefA1 == prefB1 and prefA2 == prefB2):
        return 100.0 
    if (prefA1 == "iOS" and prefB1 == "Android" or prefA1 == "Android" and prefB1 == "iOS"):
        if (prefA1 == prefB2 and prefA2 == prefB1):
            return 50.0 # both interested in mobile apps but different OS
        else:
            return 20.0 # both interested in mobile apps but different platform
    else:
        return 25.0

# overall teammate compatibility
def overallMatch(personA, personB):
    # 0.05*genderMatch + 0.1*schoolMatch + 0.1*ageMatch + 0.65*skillMatch + 0.1*appPref
    return
    # Uses weighted average. Tentatively hardcoded. Can modify later if have time
    # Above comment is just in pseudo code right now. These values are to be
    # calculated by taking in the inputs found from SQL database

