SYMTOMS_TO_IDENTIFY="""
1.	Persistent sad, anxious, or "empty" mood
2.	Feelings of hopelessness or pessimism,shows little optimism
3.	Irritability
4.	Loss of interest in activities once enjoyed
5.	Fatigue and decreased energy
6.	Difficulty concentrating, remembering, or making decisions
7.	Insomnia or poor sleep or oversleeping
8.	Changes in appetite and weight
9.	Thoughts of death or suicide
10.	Feelings of anxiety, nervousness, or inner tension
11. Levels of energy
12. Negative thoughts
"""

MEDICAL_KEY_POINTS = """
1.	Duration: How long has the patient been experiencing depressive symptoms?
2.	Onset: When did the symptoms first appear, and was there a specific triggering event?
3.	Course: Have the symptoms been continuous, intermittent, or episodic?
4.	Impact: How do the symptoms affect the patient's daily life, work, and relationships?
5.	Mood: Persistent sadness, emptiness, or hopelessness.
6.	Anhedonia: Loss of interest or pleasure in most activities.
7.	Energy: Fatigue or loss of energy.
8.	Sleep: Insomnia or hypersomnia nearly every day.
9.	Appetite: Changes in appetite or weight (increase or decrease).
10.	Cognitive: Difficulty concentrating, making decisions, or remembering things.
11.	Psychomotor: Agitation or retardation observable by others.
12.	Suicidal Ideation: Thoughts of death or suicide, or specific plans or attempts.
13.	Tension: State of persistent inner unease or anxiety that can make a person feel constantly on edge
14.	Pessimism: a tendency to see the worst aspect of things or believe that the worst will happen.
15. Feelings of failure : Frequent feelings of being a failure
"""
FINAL_RATING_GUIDELINES = {
        "0-4": "Normal/symptom absent",
        "5-9": "Mild depression",
        "10-14": "Moderate depression",
        "15-19": "Moderately Severe depression",
        "20-27": "Severe depression"
    }

PHQ9_RATING_GUIDE_LINES = {
"Mood":{
    "rating_guide_lines":"""
        Rating Guide:
            To assess feelings of being down, depressed, or hopeless, use the following scale based on patient responses:
            0: "Not at all" - No feelings of being down, depressed, or hopeless.
                Example Response: "I haven't felt down or hopeless."
            1: "Several days" - Occasional feelings of being down, depressed, or hopeless.
                "Example Response: "There were some days when I felt a bit down."
            2: "More than half the days" - Frequent feelings of being down, depressed, or hopeless, occurring more than half the days.
                Example Response: "I've felt depressed and hopeless more than half the days."
            3: "Nearly every day" - Persistent and pervasive feelings of being down, depressed, or hopeless, occurring nearly every day.
                Example Response: "Nearly every day, I feel completely hopeless."
        """, 
    "example_conversation":"""
        Doctor: I'd like to talk to you about your mood. It's important for me to understand how you've been feeling lately. Let's take it step by step together.
        Patient: I Have been feeling low from the past 10 days
        Doctor: I understand that feeling low for the past 10 days must have been really tough for you. Can you tell me more about what has been making you feel this way?
        Patient: I don't have any specific incident causing me to feel low
        Doctor: I appreciate you sharing that with me. Sometimes, feeling low can happen without a specific cause. Have you noticed any changes in your sleeping or eating patterns during this time?
        Patient: No
        Doctor: I see. Have you experienced a loss of interest in activities you usually enjoy, or have you had trouble concentrating on things?
        Patient: Yes, im not able to focus on important activates
        Doctor: I understand how difficult that must be. Have you noticed any changes in your energy levels, like feeling more tired than usual?
        Patient: Yes
        Doctor: I appreciate you sharing that with me. Have you also been feeling more irritable than usual?
        Patient: No
        Doctor: I see. It's important to recognize these changes in your mood and energy levels. Is there anything else you'd like to share about how you've been feeling?
        Patient: No
        """,
    "example_rating":"""
        {
            "1": {
                "symptoms_identified": "Persistent sad, anxious, or empty mood",
                "medical_key_points": "Duration, Impact, Mood",
                "rating": "3",
                "choice": "Nearly every day"
            },
            "section_rating": {
                "rating": "3",
                "choice": "Nearly every day"
            }
}

    """,
    "example_Symptems_key_points":""" 
        "Persistent sad, anxious, or empty mood": "Duration, Impact, Mood" 
        """ 
    },

"Anhedonia (Loss of Interest or Pleasure)":{
    "rating_guide_lines": """
        Rating Guide:
            To assess little interest or pleasure in doing things, use the following scale based on patient responses
            0: Not at all - No loss of interest or pleasure in usual activities.
            Example Response: "I haven't lost interest in activities I usually enjoy."
            1: Several days - Occasional lack of interest or pleasure in activities.
                Example Response: "There were a few days when I didn't feel like doing much."
            2: More than half the days - Frequent difficulty in enjoying activities, occurring more than half the days.
                Example Response: "Most days, I find it hard to enjoy the things I used to."
            3: Nearly every day - Persistent and pervasive lack of interest or pleasure in activities, occurring nearly every day.
                Example Response: "Almost every day, I can't find pleasure in anything I do."
        """,
    "example_conversation":""" 
        Doctor: I understand that discussing anhedonia can be challenging. Your openness to this conversation is appreciated. Now, let's talk about anhedonia and how it's been affecting you.
        Patient: Okay
        Doctor: Can you tell me about a time when you used to enjoy a particular activity, but recently found it hard to derive pleasure from it?
        Patient: I used to enjoy playing cricket, but now because of my laziness, I can't get any pleasure from it
        Doctor: It sounds like you've been feeling a lack of enjoyment from playing cricket due to a change in your motivation. Can you share more about when you first noticed this shift in your feelings towards the game?
        Patient: From past 10 days I have been facing this issue
        Doctor: I see. It's important to recognize when these changes started occurring. Can you think of any other activities or hobbies that used to bring you joy but now seem less enjoyable?
        Patient: No other activities
        Doctor: I appreciate your response. It's helpful to understand the specific impact on your interest in cricket. Can you think of any other changes in your life that may have coincided with this decrease in enjoyment from playing cricket?
        Patient: I've been dealing with a lot of stress at work, which leaves me feeling drained and unmotivated.
        Doctor: I understand that work-related stress can have a significant impact on your motivation and enjoyment of activities outside of work. It's important to address these feelings. How has this affected your overall mood and energy levels?
        Patient: The work-related stress has definitely taken a toll on my overall mood and energy levels. I often feel exhausted and irritable, even after a full night's sleep
        Doctor: I appreciate you sharing that with me. It's clear that the work-related stress is causing significant fatigue and irritability. Have you noticed any changes in your sleeping or eating patterns since this started happening?
        Patient: My sleep has become more restless, and I often wake up feeling tired
        Doctor: Thank you for sharing that. Changes in sleep patterns can significantly impact mood and energy levels. Have you noticed any changes in your appetite or weight as well?
        Patient: As for my eating habits, I've been snacking more frequently and sometimes skipping meals because I don't have the energy or appetite to eat properly
        """,
    "example_rating":"""  {"1": {"symptoms_identified": "Loss of interest in activities once enjoyed",
                                "medical_key_points": "Duration, Impact, Anhedonia",
                                "rating": "3",
                                "choice": "Nearly every day"}, 
                            "section_rating":{"rating":"3",""Nearly every day"}
                            }  
                        """ ,
    "example_Symptems_key_points":""" 
        "Loss of interest in activities once enjoyed": "Duration, Impact, Anhedonia"
        """
    },
"Sleep":{
    "rating_guide_lines":"""
        Rating Guide:
            To assess trouble falling or staying asleep, or sleeping too much, use the following scale based on patient responses:
            0: Not at all - No trouble with sleep; normal sleep patterns.
                Example Response: "My sleep has been normal."
            1: Several days - Occasional trouble with falling or staying asleep, or sleeping too much.
                Example Response: "I had trouble sleeping for a few days."
            2: More than half the days - Frequent trouble with sleep, including difficulty falling asleep, staying asleep, or sleeping too much, occurring more than half the days.
                Example Response: "Most nights, I either can't sleep or sleep too much."
            3: Nearly every day - Persistent and pervasive trouble with sleep, including significant difficulty falling asleep, staying asleep, or sleeping too much, occurring nearly every night.
                Example Response: "Almost every night, I have significant trouble sleeping."
        """,
    "example_conversation":"""
        Doctor: I understand that discussing sleep can be a sensitive topic. I'm here to listen and help you through it. Now, have you had any difficulty sleeping or found yourself sleeping too much over the past couple of weeks?
        Patient: Yes, I've had difficulty sleeping over the past couple of weeks. I've been experiencing restless nights and often wake up several times.
        Doctor: I'm sorry to hear that you've been experiencing restless nights. It can be quite challenging to deal with. Can you tell me more about any specific factors or changes in your routine that might have contributed to these sleep difficulties?
        Patient: I'm sorry to hear that you've been experiencing restless nights. It can be quite challenging to deal with. Can you tell me more about any specific factors or changes in your routine that might have contributed to these sleep difficulties?
        Doctor: I see that you are experiencing restless nights and often wake up several times. Can you share more about any specific factors or changes in your routine that might have contributed to these sleep difficulties?
        Patient: The increased workload and pressure at my job have caused a lot of stress, making it hard to unwind at night. I often find myself thinking about work even when I'm trying to sleep
        Doctor: It sounds like the increased workload and job pressure have been causing a lot of stress for you. It's understandable that this can make it hard to unwind at night. Have you noticed any other symptoms related to this increased stress, such as changes in appetite or mood?
        Patient: My appetite has become quite erratic; sometimes I feel like eating more than usual, especially unhealthy snacks, while other times I have no appetite at all and skip meals
        Doctor: I understand, it seems like the stress has been affecting your appetite as well. It's not uncommon for stress to impact eating habits. In addition to the changes in appetite, have you noticed any shifts in your mood or energy levels during the day?
        Patient: My energy levels are very low; I feel tired and drained even after getting some rest
        Doctor: I appreciate you sharing that. It's concerning to hear that your energy levels are low, and you feel tired and drained even after getting some rest. Have you been experiencing any other physical symptoms, such as headaches or muscle tension, that could be related to the stress and sleep difficulties?
        Patient: No
        Doctor: I understand. It's important to consider all aspects of your well-being. Based on what you've shared, it's clear that the increased workload and stress from your job are significantly impacting your sleep, appetite, and energy levels.
        If you ever feel the need to discuss this further or have any other concerns, I'm here to help.
        Patient: Okay
        Doctor: If you have any more questions or if there's anything else you'd like to discuss, feel free to share. Otherwise, take care and remember that I'm here to support you.
        Patient: Okay
        """,
    "example_rating":"""  {"1": {"symptoms_identified":"Insomnia or poor sleep or oversleeping",
                                        "medical_key_points":"Duration, Impact, Sleep",
                                        "rating":"2","choice":"More than half the days"},                           
                            "section_rating":{"rating":"2","choice":"More than half the days"}
                            }  
                        """,
    "example_Symptems_key_points":""" 
        "Insomnia or poor sleep or oversleeping": "Duration, Impact, Sleep" 
        """
    },
"Energy":{
    "rating_guide_lines": """
        To assess levels of energy, use the following scale based on patient responses:

            0: Not at all - No unusual tiredness; normal energy levels.
                Example Response: "I haven't felt unusually tired."
            1: Several days - Occasional feelings of tiredness or low energy.
                Example Response: "I've felt a bit tired on some days."
            2: More than half the days - Frequent feelings of tiredness and low energy, occurring more than half the days.
                Example Response: "I've felt tired and had low energy most days."
            3: Nearly every day - Persistent and pervasive feelings of exhaustion, occurring nearly every day.
                Example Response: "I feel exhausted nearly every day."
        """,
    "example_conversation":""" 
        Doctor: I understand that discussing energy levels might not seem like the most exciting topic, but it's really important for your overall well-being. Can you share with me how your energy levels have been recently?
        Patient: Recently, my energy levels have been quite low. I often wake up feeling tired,
        Doctor: I'm sorry to hear that you've been feeling this way. It must be tough to wake up feeling tired despite getting rest. Can you think of any specific factors that might be contributing to your low energy levels?
        Patient: The ongoing stress and pressure from work have been overwhelming, making it hard to relax and recharge. My sleep quality has also suffered; I often have restless nights and wake up frequently
        Doctor: It sounds like work-related stress and poor sleep quality are really taking a toll on your energy levels. It's completely understandable to feel this way. Finding a balance between work and relaxation is so important. Have you noticed any other symptoms or changes in your body that might be related to your low energy levels?
        Patient: No
        Doctor: Thank you for sharing that. It's good to know that you haven't noticed any other concerning symptoms. Understanding the full picture helps in finding the best solutions. Can you think of any specific activities or routines that have helped you manage stress and improve your energy levels in the past?
        Patient: No
        Doctor: I appreciate your honesty. Sometimes it can be challenging to find effective strategies when feeling this way. I'm here to support you in exploring different approaches to improve your energy levels. Is there anything else you'd like to share about your experience with low energy levels?
        Patient: No
        """,
    "example_rating":"""  {
                            "1": {"symptoms_identified":"Levels of energy",
                                "medical_key_points":"Duration, Impact, Energy",
                                "rating":"2","choice":"More than half the days"
                                },                                        
                            "section_rating":{"rating":"2","choice":"More than half the days"}
                            }  
                                    """,
    "example_Symptems_key_points":""" 
        "Levels of energy": "Duration, Impact, Energy" 
        """
    },

"Appetite":{
    "rating_guide_lines":"""
        Rating Guide:
        To assess changes in appetite, use the following scale based on patient responses:

        0: Not at all - No changes in appetite; normal eating patterns.
            Example Response: "My appetite has been normal."
        1: Several days - Occasional changes in appetite, including poor appetite or overeating.
            Example Response: "I had a few days with a poor appetite or overeating."
        2: More than half the days - Frequent changes in appetite, including not feeling like eating or eating too much, occurring more than half the days.
            Example Response: "Most days, I either don't feel like eating or I eat too much."
        3: Nearly every day - Persistent and pervasive changes in appetite, including poor appetite or overeating, occurring nearly every day.
            Example Response: "Nearly every day, I have a poor appetite or I overeat."
        """,
    "example_conversation":""" 
        Doctor: Hello! In this section, I'd like to discuss your appetite. How have your eating habits been lately? Have you noticed any changes in your appetite, such as not feeling hungry at all or overeating?
        Patient: I've noticed that my appetite has become quite unpredictable. Some days, I don't feel hungry at all and end up skipping meals, while on other days, I find myself overeating, especially unhealthy snacks
        Doctor: It sounds like your appetite has been quite erratic, with fluctuations between not feeling hungry at all and overeating. This can definitely impact your overall well-being. Can you think of any specific factors or situations that might be contributing to these changes in your appetite?
        Patient: The primary factor is the increased stress and pressure from work, which has been overwhelming and makes it difficult to maintain a regular eating schedule. When I'm particularly stressed or anxious, I tend to lose my appetite.
        Doctor: I understand how work-related stress can significantly affect your appetite. It's common for stress and anxiety to impact eating habits. Have you noticed any other symptoms or changes in your overall well-being that coincide with these periods of increased stress?
        Patient: no
        Doctor: I appreciate your response. Stress can indeed have a significant impact on appetite. Have you found any strategies that have helped you cope with stress in the past?
        Patient: Regular exercise, like going for a run or playing sports, has always been a great way to release tension and improve my mood.
        Doctor: Regular exercise can be an excellent way to manage stress and improve overall well-being. It's great to hear that physical activity has been helpful for you. Is there anything else you've tried or considered to help manage your stress levels and improve your appetite?
        Patient: no
        Doctor: I understand. It's important to find strategies that work best for you. Your insight into the impact of stress on your appetite is valuable. Is there anything else you'd like to share about your appetite or related concerns?
        Patient: no
        """,
    "example_rating":"""  {"1": {"symptoms_identified":"Changes in appetite",
                                        "medical_key_points":"Duration, Impact, Appetite",
                                        "rating":"2","choice":"More than half the days"},                                       
                            "section_rating":{"rating":"2","choice":"More than half the days"}
                           }  
                    """,
    "example_Symptems_key_points":"""
        "Changes in appetite": "Duration, Impact, Appetite"
        """
},

"Self-Worth":{
    "rating_guide_lines":"""
        Rating Guide:
        To assess feelings of being a failure, use the following scale based on patient responses:
        0: Not at all - No feelings of being a failure.
            Example Response: "I haven't felt this way."
        1: Several days - Occasional feelings of being a failure.
            Example Response: "On a few days, I felt like a failure."
        2: More than half the days - Frequent feelings of being a failure, occurring more than half the days.
            Example Response: "I've often felt bad about myself."
        3: Nearly every day - Persistent and pervasive feelings of being a failure, occurring nearly every day.
            Example Response: "I feel like a failure almost every day."
        """,
    "example_conversation": """ 
        Doctor: I understand that discussing self-worth can be a sensitive topic. Your feelings and experiences are important, and I'm here to listen and support you. Is there anything specific you'd like to share about how you've been feeling about yourself recently?
        Patient: I've been struggling with feelings of low self-worth. The stress and pressure from work have made me feel like I'm not performing well enough, which has affected my confidence.
        Doctor: I can understand how the pressure from work can take a toll on your confidence and self-worth. It sounds like you've been dealing with a lot. Can you tell me more about the specific situations at work that have been making you feel this way?
        Patient: One major issue is the increased workload and tight deadlines. I often find myself working late into the night to keep up, which leaves me feeling exhausted and overwhelmed. Additionally, there have been a few projects where I've received critical feedback from my supervisors, which has made me doubt my abilities
        Doctor: It sounds like you've been dealing with a lot of stress and pressure from the increased workload and critical feedback. It's completely understandable that these situations have impacted your confidence. How have these experiences been affecting your overall well-being and how you perceive yourself outside of work?
        Patient: The constant stress and pressure have left me feeling mentally and physically exhausted, which affects my ability to enjoy activities I once loved.
        Doctor: I can see how the stress and exhaustion have taken a toll on your overall well-being, impacting your ability to enjoy activities outside of work. It's important to address these feelings and find ways to support your mental and physical health. Have you been able to talk to anyone about these feelings, either friends, family, or a professional?
        Patient: NO
        Doctor: It's completely okay to feel hesitant about discussing these feelings, but it's important to have a support system in place. Would you be open to exploring ways to manage stress and improve your self-worth, such as seeking support from a trusted friend, family member, or professional?
        Patient: I'm open to seeking support from a trusted friend or family member, as talking about these issues can provide some relief
        Doctor: That's a positive step. Opening up to someone you trust can make a significant difference in how you're feeling. Is there anything specific you'd like to discuss with your friend or family member, or are you looking for general support and understanding?
        Patient: No
        """,
    "example_rating":"""  {"1": {"symptoms_identified":"Negative thoughts",
                                        "medical_key_points":"Feelings of failure, Duration, Impact",
                                        "rating":"2","choice":"More than half the days"},                           
                            "section_rating":{"rating":"2","choice":"More than half the days"}
                            }  
                            """,
    "example_Symptems_key_points":""" 
        "Negative thoughts":"Feelings of failure, Duration, Impact"
        """
    },

"Cognitive Function":{
    "rating_guide_lines":"""
        Rating Guide:
        To assess trouble concentrating, use the following scale based on patient responses:

        0: Not at all- No trouble concentrating.
            Example Response: "I haven't had trouble concentrating."
        1: Several days- Occasional trouble focusing.
            Example Response: "There were a few days when I had trouble focusing."
        2: More than half the days- Frequent difficulty concentrating, occurring more than half the days.
            Example Response: "Most days, I can't concentrate well."
        3: Nearly every day- Persistent and pervasive difficulty focusing, occurring nearly every day.
            Example Response: "Almost every day, I find it very hard to focus."
        """,
    "example_conversation": """ 
        Doctor: Hello! In this section, we'll be discussing cognitive function. Have you noticed any changes in your ability to concentrate or remember things recently?
        Patient: My ability to concentrate has decreased significantly; I often find myself easily distracted and struggling to focus on tasks, both at work and in my personal life
        Doctor: I understand how challenging that must be. It can be frustrating to feel like your concentration is slipping. Can you tell me more about when you first noticed this change in your ability to concentrate?
        Patient: I first noticed the change in my ability to concentrate a few weeks ago, around the time when my workload increased significantly. I started having trouble focusing during meetings and found it difficult to stay on task while working on projects.
        Doctor: I see, it sounds like the increase in workload may have contributed to these difficulties. Have you experienced any other changes in your cognitive function, such as forgetfulness or trouble making decisions?
        Patient: Yes I have
        Doctor: I appreciate your response. Could you provide more details about the specific changes you've noticed in your memory and decision-making abilities?
        Patient: I've been more forgetful, often losing track of details and deadlines. My decision-making has become slower and less confident, making even simple choices feel overwhelming.
        Doctor: Thank you for sharing that. It's understandable that these changes are causing some concern. Have you noticed any other cognitive changes, such as difficulty with problem-solving or processing information?
        Patient: no
        """,
    "example_rating":"""  {"1": {"symptoms_identified":"Difficulty concentrating, remembering, or making decisions",
                                        "medical_key_points":"Duration, Impact, Cognitive function",
                                        "rating":"3","choice":"Nearly every day"},                                       
                            "section_rating":{"rating":"3","choice":"Nearly every day"}
                            }  
                        """,
    "example_Symptems_key_points": """ 
        "Difficulty concentrating, remembering, or making decisions":"Duration, Impact, Cognitive function"
        """    
    },

"Psychomotor Changes":{
    "rating_guide_lines":"""
        Rating Guide:
        To assess changes in movement or speech, use the following scale based on patient responses:
        0: Not at all - No noticeable changes in movement or speech.
            Example Response: "I haven't noticed any changes in my movement or speech."
        1: Several days - Occasional changes in movement or speech, such as feeling more restless or sluggish on some days.
            Example Response: "Some days, I've been more restless or sluggish."
        2: More than half the days - Frequent changes in movement or speech, noticeable to others on most days.
            Example Response: "Most days, others might notice I move or speak differently."
        3: Nearly every day - Persistent and pervasive changes in movement or speech, noticeable almost every day.
            Example Response: "Nearly every day, my movements or speech changes are noticeable."
        """,
    "example_conversation":""" 
        Doctor: I understand that discussing health-related topics can sometimes feel overwhelming. I'm here to help you through this. Let's take it step by step together. Now, have you experienced any changes in your movements or speech, like feeling really slow or restless and fidgety compared to usual?
        Patient: No, I don't have any issues with movements or speech
        Doctor: I appreciate your response. Even though you haven't noticed any changes in your movements or speech, it's important to explore all possibilities. Have you noticed any other unusual physical sensations or changes in your daily routine that you'd like to discuss?
        Patient: No
        Doctor: I see, thank you for sharing that. It's important to consider all aspects of your health. If you do happen to notice any changes in the future, please don't hesitate to reach out. Your well-being is important, and I'm here to support you. If you have any other concerns or questions about your health, feel free to share them.
        Patient: Okay
        """,
    "example_rating":"""  {"1": {"symptoms_identified":"No symptoms identified",
                                        "medical_key_points":"No medical key points identified",
                                        "rating":"0","choice":"Not at all"},                                        
                                "section_rating":{"rating":"0","choice":"Not at all"}
                                }  
        """,
    "example_Symptems_key_points":""" 
        "No symptoms identified":"No medical key points identified"
        """   
    },
"Suicidal Ideation":{
    "rating_guide_lines": """
        Rating Guide:

        To assess thoughts of self-harm or being better off dead, use the following scale based on patient responses:
        0: Not at all - No thoughts of self-harm or being better off dead.
            Example Response: "I haven't had any thoughts like that."
        1: Several days - Occasional thoughts of self-harm or being better off dead on a few days.
            Example Response: "I've had such thoughts on a few days."
        2: More than half the days - Frequent thoughts of self-harm or being better off dead, occurring more than half the days.
            Example Response: "I've had these thoughts more than half the days."
        3: Nearly every day - Persistent and pervasive thoughts of self-harm or being better off dead, occurring nearly every day.
            Example Response: "Nearly every day, I think I'd be better off dead or have thoughts of self-harm."
        """,
    "example_conversation":""" 
        Doctor: I understand that discussing this topic can be difficult. I'm here to listen and support you. Now, have you had any thoughts about wanting to escape life or hurting yourself in any way over the past couple of weeks?
        Patient: Over the past couple of weeks, I haven't had any thoughts about wanting to escape life or hurting myself.
        Doctor: I appreciate you sharing that with me. It's important to have an open conversation about these feelings. Can you tell me about any other emotions or thoughts you've been experiencing lately that have been challenging for you?
        Patient: I often feel frustrated and disappointed in myself, especially when I'm unable to meet work expectations or enjoy activities I used to love
        Doctor: It's completely understandable to feel frustrated and disappointed, especially when things aren't going as planned. It's important to acknowledge these emotions. Can you share more about the specific work expectations or activities that have been challenging for you?
        Patient: At work, the increased workload and tight deadlines have been particularly challenging
        Doctor: I hear you. It sounds like work has been very demanding lately. How has this been affecting your overall well-being and daily life?
        Patient: making it hard to enjoy activities or spend quality time with friends and family
        Doctor: I can understand how that would be difficult. It's important to have a work-life balance and to be able to enjoy time with loved ones. Have you been able to find any moments of relief or relaxation, even in the midst of these challenges?
        Patient: No
        Doctor: I'm sorry to hear that. It's important to find ways to take care of yourself, especially during tough times. Is there anything specific that you've tried in the past to help manage stress or find moments of relaxation?
        Patient: No
        Doctor: I appreciate your honesty. It can be hard to find the right strategies, but it's important to keep exploring different options. Is there anything else you'd like to share about how you've been feeling or any concerns you have?
        Patient: No
        """,
    "example_rating":"""  {"1": {"symptoms_identified":"Thoughts of death or suicide",
                                "medical_key_points":"Duration, Impact, Specific plans or attempts",
                                "rating":"0","choice":"Not at all"},
                            "section_rating":{"rating":"0","choice":"Not at all"}
                        }  
                    """,
    "example_Symptems_key_points":""" 
        "Thoughts of death or suicide":"Duration, Impact, Specific plans or attempts"
        """
    }        
}


PHQ9_RATING_GUIDE_LINES_V1 = {
"Mood":{
    "rating_guide_lines":"""
        Rating Guide:
            To assess feelings of being down, depressed, or hopeless, use the following scale based on patient responses:
            0: "Not at all" - No feelings of being down, depressed, or hopeless.
                Example Response: "I haven't felt down or hopeless."
            1: "Several days" - Occasional feelings of being down, depressed, or hopeless.
                "Example Response: "There were some days when I felt a bit down."
            2: "More than half the days" - Frequent feelings of being down, depressed, or hopeless, occurring more than half the days.
                Example Response: "I've felt depressed and hopeless more than half the days."
            3: "Nearly every day" - Persistent and pervasive feelings of being down, depressed, or hopeless, occurring nearly every day.
                Example Response: "Nearly every day, I feel completely hopeless."
        """, 
    "example_conversation":"""
        Doctor: I'd like to talk to you about your mood. It's important for me to understand how you've been feeling lately. Let's take it step by step together.
        Patient: I Have been feeling low from the past 10 days
        Doctor: I understand that feeling low for the past 10 days must have been really tough for you. Can you tell me more about what has been making you feel this way?
        Patient: I don't have any specific incident causing me to feel low
        Doctor: I appreciate you sharing that with me. Sometimes, feeling low can happen without a specific cause. Have you noticed any changes in your sleeping or eating patterns during this time?
        Patient: No
        Doctor: I see. Have you experienced a loss of interest in activities you usually enjoy, or have you had trouble concentrating on things?
        Patient: Yes, im not able to focus on important activates
        Doctor: I understand how difficult that must be. Have you noticed any changes in your energy levels, like feeling more tired than usual?
        Patient: Yes
        Doctor: I appreciate you sharing that with me. Have you also been feeling more irritable than usual?
        Patient: No
        Doctor: I see. It's important to recognize these changes in your mood and energy levels. Is there anything else you'd like to share about how you've been feeling?
        Patient: No
        """,
    "example_rating":"""
                    {         
                    "section_rating": {
                        "rating": "3",
                        "choice": "Nearly every day"
                    }
                }
                    """,
    "example_Symptems_key_points":""" 
        "Persistent sad, anxious, or empty mood": "Duration, Impact, Mood" 
        """ 
    },

"Anhedonia (Loss of Interest or Pleasure)":{
    "rating_guide_lines": """
        Rating Guide:
            To assess little interest or pleasure in doing things, use the following scale based on patient responses
            0: Not at all - No loss of interest or pleasure in usual activities.
            Example Response: "I haven't lost interest in activities I usually enjoy."
            1: Several days - Occasional lack of interest or pleasure in activities.
                Example Response: "There were a few days when I didn't feel like doing much."
            2: More than half the days - Frequent difficulty in enjoying activities, occurring more than half the days.
                Example Response: "Most days, I find it hard to enjoy the things I used to."
            3: Nearly every day - Persistent and pervasive lack of interest or pleasure in activities, occurring nearly every day.
                Example Response: "Almost every day, I can't find pleasure in anything I do."
        """,
    "example_conversation":""" 
        Doctor: I understand that discussing anhedonia can be challenging. Your openness to this conversation is appreciated. Now, let's talk about anhedonia and how it's been affecting you.
        Patient: Okay
        Doctor: Can you tell me about a time when you used to enjoy a particular activity, but recently found it hard to derive pleasure from it?
        Patient: I used to enjoy playing cricket, but now because of my laziness, I can't get any pleasure from it
        Doctor: It sounds like you've been feeling a lack of enjoyment from playing cricket due to a change in your motivation. Can you share more about when you first noticed this shift in your feelings towards the game?
        Patient: From past 10 days I have been facing this issue
        Doctor: I see. It's important to recognize when these changes started occurring. Can you think of any other activities or hobbies that used to bring you joy but now seem less enjoyable?
        Patient: No other activities
        Doctor: I appreciate your response. It's helpful to understand the specific impact on your interest in cricket. Can you think of any other changes in your life that may have coincided with this decrease in enjoyment from playing cricket?
        Patient: I've been dealing with a lot of stress at work, which leaves me feeling drained and unmotivated.
        Doctor: I understand that work-related stress can have a significant impact on your motivation and enjoyment of activities outside of work. It's important to address these feelings. How has this affected your overall mood and energy levels?
        Patient: The work-related stress has definitely taken a toll on my overall mood and energy levels. I often feel exhausted and irritable, even after a full night's sleep
        Doctor: I appreciate you sharing that with me. It's clear that the work-related stress is causing significant fatigue and irritability. Have you noticed any changes in your sleeping or eating patterns since this started happening?
        Patient: My sleep has become more restless, and I often wake up feeling tired
        Doctor: Thank you for sharing that. Changes in sleep patterns can significantly impact mood and energy levels. Have you noticed any changes in your appetite or weight as well?
        Patient: As for my eating habits, I've been snacking more frequently and sometimes skipping meals because I don't have the energy or appetite to eat properly
        """,
    "example_rating":"""  {
                            'section_rating':{
                            "rating":"3",
                            "choice":"Nearly every day"
                            }
                        }  
                        """ ,
    "example_Symptems_key_points":""" 
        "Loss of interest in activities once enjoyed": "Duration, Impact, Anhedonia"
        """
    },
"Sleep":{
    "rating_guide_lines":"""
        Rating Guide:
            To assess trouble falling or staying asleep, or sleeping too much, use the following scale based on patient responses:
            0: Not at all - No trouble with sleep; normal sleep patterns.
                Example Response: "My sleep has been normal."
            1: Several days - Occasional trouble with falling or staying asleep, or sleeping too much.
                Example Response: "I had trouble sleeping for a few days."
            2: More than half the days - Frequent trouble with sleep, including difficulty falling asleep, staying asleep, or sleeping too much, occurring more than half the days.
                Example Response: "Most nights, I either can't sleep or sleep too much."
            3: Nearly every day - Persistent and pervasive trouble with sleep, including significant difficulty falling asleep, staying asleep, or sleeping too much, occurring nearly every night.
                Example Response: "Almost every night, I have significant trouble sleeping."
        """,
    "example_conversation":"""
        Doctor: I understand that discussing sleep can be a sensitive topic. I'm here to listen and help you through it. Now, have you had any difficulty sleeping or found yourself sleeping too much over the past couple of weeks?
        Patient: Yes, I've had difficulty sleeping over the past couple of weeks. I've been experiencing restless nights and often wake up several times.
        Doctor: I'm sorry to hear that you've been experiencing restless nights. It can be quite challenging to deal with. Can you tell me more about any specific factors or changes in your routine that might have contributed to these sleep difficulties?
        Patient: I'm sorry to hear that you've been experiencing restless nights. It can be quite challenging to deal with. Can you tell me more about any specific factors or changes in your routine that might have contributed to these sleep difficulties?
        Doctor: I see that you are experiencing restless nights and often wake up several times. Can you share more about any specific factors or changes in your routine that might have contributed to these sleep difficulties?
        Patient: The increased workload and pressure at my job have caused a lot of stress, making it hard to unwind at night. I often find myself thinking about work even when I'm trying to sleep
        Doctor: It sounds like the increased workload and job pressure have been causing a lot of stress for you. It's understandable that this can make it hard to unwind at night. Have you noticed any other symptoms related to this increased stress, such as changes in appetite or mood?
        Patient: My appetite has become quite erratic; sometimes I feel like eating more than usual, especially unhealthy snacks, while other times I have no appetite at all and skip meals
        Doctor: I understand, it seems like the stress has been affecting your appetite as well. It's not uncommon for stress to impact eating habits. In addition to the changes in appetite, have you noticed any shifts in your mood or energy levels during the day?
        Patient: My energy levels are very low; I feel tired and drained even after getting some rest
        Doctor: I appreciate you sharing that. It's concerning to hear that your energy levels are low, and you feel tired and drained even after getting some rest. Have you been experiencing any other physical symptoms, such as headaches or muscle tension, that could be related to the stress and sleep difficulties?
        Patient: No
        Doctor: I understand. It's important to consider all aspects of your well-being. Based on what you've shared, it's clear that the increased workload and stress from your job are significantly impacting your sleep, appetite, and energy levels.
        If you ever feel the need to discuss this further or have any other concerns, I'm here to help.
        Patient: Okay
        Doctor: If you have any more questions or if there's anything else you'd like to discuss, feel free to share. Otherwise, take care and remember that I'm here to support you.
        Patient: Okay
        """,
    "example_rating":"""  {                          
                            'section_rating':{"rating":"2","choice":"More than half the days"}
                            }  
                        """,
    "example_Symptems_key_points":""" 
        "Insomnia or poor sleep or oversleeping": "Duration, Impact, Sleep" 
        """
    },
"Energy":{
    "rating_guide_lines": """
        To assess levels of energy, use the following scale based on patient responses:

            0: Not at all - No unusual tiredness; normal energy levels.
                Example Response: "I haven't felt unusually tired."
            1: Several days - Occasional feelings of tiredness or low energy.
                Example Response: "I've felt a bit tired on some days."
            2: More than half the days - Frequent feelings of tiredness and low energy, occurring more than half the days.
                Example Response: "I've felt tired and had low energy most days."
            3: Nearly every day - Persistent and pervasive feelings of exhaustion, occurring nearly every day.
                Example Response: "I feel exhausted nearly every day."
        """,
    "example_conversation":""" 
        Doctor: I understand that discussing energy levels might not seem like the most exciting topic, but it's really important for your overall well-being. Can you share with me how your energy levels have been recently?
        Patient: Recently, my energy levels have been quite low. I often wake up feeling tired,
        Doctor: I'm sorry to hear that you've been feeling this way. It must be tough to wake up feeling tired despite getting rest. Can you think of any specific factors that might be contributing to your low energy levels?
        Patient: The ongoing stress and pressure from work have been overwhelming, making it hard to relax and recharge. My sleep quality has also suffered; I often have restless nights and wake up frequently
        Doctor: It sounds like work-related stress and poor sleep quality are really taking a toll on your energy levels. It's completely understandable to feel this way. Finding a balance between work and relaxation is so important. Have you noticed any other symptoms or changes in your body that might be related to your low energy levels?
        Patient: No
        Doctor: Thank you for sharing that. It's good to know that you haven't noticed any other concerning symptoms. Understanding the full picture helps in finding the best solutions. Can you think of any specific activities or routines that have helped you manage stress and improve your energy levels in the past?
        Patient: No
        Doctor: I appreciate your honesty. Sometimes it can be challenging to find effective strategies when feeling this way. I'm here to support you in exploring different approaches to improve your energy levels. Is there anything else you'd like to share about your experience with low energy levels?
        Patient: No
        """,
    "example_rating":"""  {                                                                 
                            'section_rating':{"rating":"2","choice":"More than half the days"}
                            }  
                    """,
    "example_Symptems_key_points":""" 
        "Levels of energy": "Duration, Impact, Energy" 
        """
    },

"Appetite":{
    "rating_guide_lines":"""
        Rating Guide:
        To assess changes in appetite, use the following scale based on patient responses:

        0: Not at all - No changes in appetite; normal eating patterns.
            Example Response: "My appetite has been normal."
        1: Several days - Occasional changes in appetite, including poor appetite or overeating.
            Example Response: "I had a few days with a poor appetite or overeating."
        2: More than half the days - Frequent changes in appetite, including not feeling like eating or eating too much, occurring more than half the days.
            Example Response: "Most days, I either don't feel like eating or I eat too much."
        3: Nearly every day - Persistent and pervasive changes in appetite, including poor appetite or overeating, occurring nearly every day.
            Example Response: "Nearly every day, I have a poor appetite or I overeat."
        """,
    "example_conversation":""" 
        Doctor: Hello! In this section, I'd like to discuss your appetite. How have your eating habits been lately? Have you noticed any changes in your appetite, such as not feeling hungry at all or overeating?
        Patient: I've noticed that my appetite has become quite unpredictable. Some days, I don't feel hungry at all and end up skipping meals, while on other days, I find myself overeating, especially unhealthy snacks
        Doctor: It sounds like your appetite has been quite erratic, with fluctuations between not feeling hungry at all and overeating. This can definitely impact your overall well-being. Can you think of any specific factors or situations that might be contributing to these changes in your appetite?
        Patient: The primary factor is the increased stress and pressure from work, which has been overwhelming and makes it difficult to maintain a regular eating schedule. When I'm particularly stressed or anxious, I tend to lose my appetite.
        Doctor: I understand how work-related stress can significantly affect your appetite. It's common for stress and anxiety to impact eating habits. Have you noticed any other symptoms or changes in your overall well-being that coincide with these periods of increased stress?
        Patient: no
        Doctor: I appreciate your response. Stress can indeed have a significant impact on appetite. Have you found any strategies that have helped you cope with stress in the past?
        Patient: Regular exercise, like going for a run or playing sports, has always been a great way to release tension and improve my mood.
        Doctor: Regular exercise can be an excellent way to manage stress and improve overall well-being. It's great to hear that physical activity has been helpful for you. Is there anything else you've tried or considered to help manage your stress levels and improve your appetite?
        Patient: no
        Doctor: I understand. It's important to find strategies that work best for you. Your insight into the impact of stress on your appetite is valuable. Is there anything else you'd like to share about your appetite or related concerns?
        Patient: no
        """,
    "example_rating":"""  {                                      
                            "section_rating":{"rating":"2","choice":"More than half the days"}
                           }  
                    """,
    "example_Symptems_key_points":"""
        "Changes in appetite": "Duration, Impact, Appetite"
        """
},

"Self-Worth":{
    "rating_guide_lines":"""
        Rating Guide:
        To assess feelings of being a failure, use the following scale based on patient responses:
        0: Not at all - No feelings of being a failure.
            Example Response: "I haven't felt this way."
        1: Several days - Occasional feelings of being a failure.
            Example Response: "On a few days, I felt like a failure."
        2: More than half the days - Frequent feelings of being a failure, occurring more than half the days.
            Example Response: "I've often felt bad about myself."
        3: Nearly every day - Persistent and pervasive feelings of being a failure, occurring nearly every day.
            Example Response: "I feel like a failure almost every day."
        """,
    "example_conversation": """ 
        Doctor: I understand that discussing self-worth can be a sensitive topic. Your feelings and experiences are important, and I'm here to listen and support you. Is there anything specific you'd like to share about how you've been feeling about yourself recently?
        Patient: I've been struggling with feelings of low self-worth. The stress and pressure from work have made me feel like I'm not performing well enough, which has affected my confidence.
        Doctor: I can understand how the pressure from work can take a toll on your confidence and self-worth. It sounds like you've been dealing with a lot. Can you tell me more about the specific situations at work that have been making you feel this way?
        Patient: One major issue is the increased workload and tight deadlines. I often find myself working late into the night to keep up, which leaves me feeling exhausted and overwhelmed. Additionally, there have been a few projects where I've received critical feedback from my supervisors, which has made me doubt my abilities
        Doctor: It sounds like you've been dealing with a lot of stress and pressure from the increased workload and critical feedback. It's completely understandable that these situations have impacted your confidence. How have these experiences been affecting your overall well-being and how you perceive yourself outside of work?
        Patient: The constant stress and pressure have left me feeling mentally and physically exhausted, which affects my ability to enjoy activities I once loved.
        Doctor: I can see how the stress and exhaustion have taken a toll on your overall well-being, impacting your ability to enjoy activities outside of work. It's important to address these feelings and find ways to support your mental and physical health. Have you been able to talk to anyone about these feelings, either friends, family, or a professional?
        Patient: NO
        Doctor: It's completely okay to feel hesitant about discussing these feelings, but it's important to have a support system in place. Would you be open to exploring ways to manage stress and improve your self-worth, such as seeking support from a trusted friend, family member, or professional?
        Patient: I'm open to seeking support from a trusted friend or family member, as talking about these issues can provide some relief
        Doctor: That's a positive step. Opening up to someone you trust can make a significant difference in how you're feeling. Is there anything specific you'd like to discuss with your friend or family member, or are you looking for general support and understanding?
        Patient: No
        """,
    "example_rating":"""  {                     
                            "section_rating":{"rating":"2","choice":"More than half the days"}
                            }  
                            """,
    "example_Symptems_key_points":""" 
        "Negative thoughts":"Feelings of failure, Duration, Impact"
        """
    },

"Cognitive Function":{
    "rating_guide_lines":"""
        Rating Guide:
        To assess trouble concentrating, use the following scale based on patient responses:

        0: Not at all- No trouble concentrating.
            Example Response: "I haven't had trouble concentrating."
        1: Several days- Occasional trouble focusing.
            Example Response: "There were a few days when I had trouble focusing."
        2: More than half the days- Frequent difficulty concentrating, occurring more than half the days.
            Example Response: "Most days, I can't concentrate well."
        3: Nearly every day- Persistent and pervasive difficulty focusing, occurring nearly every day.
            Example Response: "Almost every day, I find it very hard to focus."
        """,
    "example_conversation": """ 
        Doctor: Hello! In this section, we'll be discussing cognitive function. Have you noticed any changes in your ability to concentrate or remember things recently?
        Patient: My ability to concentrate has decreased significantly; I often find myself easily distracted and struggling to focus on tasks, both at work and in my personal life
        Doctor: I understand how challenging that must be. It can be frustrating to feel like your concentration is slipping. Can you tell me more about when you first noticed this change in your ability to concentrate?
        Patient: I first noticed the change in my ability to concentrate a few weeks ago, around the time when my workload increased significantly. I started having trouble focusing during meetings and found it difficult to stay on task while working on projects.
        Doctor: I see, it sounds like the increase in workload may have contributed to these difficulties. Have you experienced any other changes in your cognitive function, such as forgetfulness or trouble making decisions?
        Patient: Yes I have
        Doctor: I appreciate your response. Could you provide more details about the specific changes you've noticed in your memory and decision-making abilities?
        Patient: I've been more forgetful, often losing track of details and deadlines. My decision-making has become slower and less confident, making even simple choices feel overwhelming.
        Doctor: Thank you for sharing that. It's understandable that these changes are causing some concern. Have you noticed any other cognitive changes, such as difficulty with problem-solving or processing information?
        Patient: no
        """,
    "example_rating":"""  {                                     
                            "section_rating":{"rating":"3","choice":"Nearly every day"}
                            }  
                        """,
    "example_Symptems_key_points": """ 
        "Difficulty concentrating, remembering, or making decisions":"Duration, Impact, Cognitive function"
        """    
    },

"Psychomotor Changes":{
    "rating_guide_lines":"""
        Rating Guide:
        To assess changes in movement or speech, use the following scale based on patient responses:
        0: Not at all - No noticeable changes in movement or speech.
            Example Response: "I haven't noticed any changes in my movement or speech."
        1: Several days - Occasional changes in movement or speech, such as feeling more restless or sluggish on some days.
            Example Response: "Some days, I've been more restless or sluggish."
        2: More than half the days - Frequent changes in movement or speech, noticeable to others on most days.
            Example Response: "Most days, others might notice I move or speak differently."
        3: Nearly every day - Persistent and pervasive changes in movement or speech, noticeable almost every day.
            Example Response: "Nearly every day, my movements or speech changes are noticeable."
        """,
    "example_conversation":""" 
        Doctor: I understand that discussing health-related topics can sometimes feel overwhelming. I'm here to help you through this. Let's take it step by step together. Now, have you experienced any changes in your movements or speech, like feeling really slow or restless and fidgety compared to usual?
        Patient: No, I don't have any issues with movements or speech
        Doctor: I appreciate your response. Even though you haven't noticed any changes in your movements or speech, it's important to explore all possibilities. Have you noticed any other unusual physical sensations or changes in your daily routine that you'd like to discuss?
        Patient: No
        Doctor: I see, thank you for sharing that. It's important to consider all aspects of your health. If you do happen to notice any changes in the future, please don't hesitate to reach out. Your well-being is important, and I'm here to support you. If you have any other concerns or questions about your health, feel free to share them.
        Patient: Okay
        """,
    "example_rating":"""  {
                            "section_rating":{"rating":"0","choice":"Not at all"}
                        }  
        """,
    "example_Symptems_key_points":""" 
        "No symptoms identified":"No medical key points identified"
        """   
    },
"Suicidal Ideation":{
    "rating_guide_lines": """
        Rating Guide:

        To assess thoughts of self-harm or being better off dead, use the following scale based on patient responses:
        0: Not at all - No thoughts of self-harm or being better off dead.
            Example Response: "I haven't had any thoughts like that."
        1: Several days - Occasional thoughts of self-harm or being better off dead on a few days.
            Example Response: "I've had such thoughts on a few days."
        2: More than half the days - Frequent thoughts of self-harm or being better off dead, occurring more than half the days.
            Example Response: "I've had these thoughts more than half the days."
        3: Nearly every day - Persistent and pervasive thoughts of self-harm or being better off dead, occurring nearly every day.
            Example Response: "Nearly every day, I think I'd be better off dead or have thoughts of self-harm."
        """,
    "example_conversation":""" 
        Doctor: I understand that discussing this topic can be difficult. I'm here to listen and support you. Now, have you had any thoughts about wanting to escape life or hurting yourself in any way over the past couple of weeks?
        Patient: Over the past couple of weeks, I haven't had any thoughts about wanting to escape life or hurting myself.
        Doctor: I appreciate you sharing that with me. It's important to have an open conversation about these feelings. Can you tell me about any other emotions or thoughts you've been experiencing lately that have been challenging for you?
        Patient: I often feel frustrated and disappointed in myself, especially when I'm unable to meet work expectations or enjoy activities I used to love
        Doctor: It's completely understandable to feel frustrated and disappointed, especially when things aren't going as planned. It's important to acknowledge these emotions. Can you share more about the specific work expectations or activities that have been challenging for you?
        Patient: At work, the increased workload and tight deadlines have been particularly challenging
        Doctor: I hear you. It sounds like work has been very demanding lately. How has this been affecting your overall well-being and daily life?
        Patient: making it hard to enjoy activities or spend quality time with friends and family
        Doctor: I can understand how that would be difficult. It's important to have a work-life balance and to be able to enjoy time with loved ones. Have you been able to find any moments of relief or relaxation, even in the midst of these challenges?
        Patient: No
        Doctor: I'm sorry to hear that. It's important to find ways to take care of yourself, especially during tough times. Is there anything specific that you've tried in the past to help manage stress or find moments of relaxation?
        Patient: No
        Doctor: I appreciate your honesty. It can be hard to find the right strategies, but it's important to keep exploring different options. Is there anything else you'd like to share about how you've been feeling or any concerns you have?
        Patient: No
        """,
    "example_rating":"""  {
                            "section_rating":{"rating":"0","choice":"Not at all"}
                        }  
                    """,
    "example_Symptems_key_points":""" 
        "Thoughts of death or suicide":"Duration, Impact, Specific plans or attempts"
        """
    }        
}