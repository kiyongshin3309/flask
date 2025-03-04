# word_list.py

word_data = {
    "초등학생": {
        "1월": {
            "한글": ["여호와는 나의 목자시니 내게 부족함이 없으리로다", "주님은 선하시고 인자하심이 영원하다"],
            "영문": ["The Lord is my shepherd, I shall not want", "The Lord is good and his love endures forever"]
        },
        "2월": {
            "한글": ["하나님은 사랑이시라", "내 길을 여호와께 맡기라"],
            "영문": ["God is love", "Commit your way to the Lord"]
        }
    },
    "중학생": {
        "1월": {
            "한글": ["네 마음을 다하여 여호와를 신뢰하고", "주의 말씀은 내 발의 등이요"],
            "영문": ["Trust in the Lord with all your heart", "Your word is a lamp to my feet"]
        }
    },
    "고등학생": {
        "1월": {
            "한글": ["오직 너는 마음을 강하게 하고 담대히 하라", "여호와를 경외하는 것이 지혜의 근본이니라"],
            "영문": ["Be strong and courageous", "The fear of the Lord is the beginning of wisdom"]
        }
    }
}

def get_word_list(student_level, month, language):
    return word_data.get(student_level, {}).get(month, {}).get(language, [])
