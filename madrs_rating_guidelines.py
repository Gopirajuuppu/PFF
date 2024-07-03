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
"""
FINAL_RATING_GUIDELINES = {
        "0-6": "Normal/symptom absent",
        "7-19": "Mild depression",
        "20-34": "Moderate depression",
        "35-60": "Severe depression"
    }
MADRS_RATING_GUIDE_LINES = {
"APPARENT_SADNESS":{
    "rating_guide_lines":"""
        Apparent Sadness Rating Guide:
        To assess apparent sadness, use the following scale based on patient responses:

            0: No sadness. The patient appears fine and expresses no feelings of sadness.
                Example Response: "I feel fine most of the time."
            1: Slight sadness. The patient rarely feels sad, and it has minimal impact.
                Example Response: "I feel sad occasionally, but it's not a big deal."
            2: Mild sadness. The patient sometimes feels sad, but it does not affect daily life significantly.
                Example Response: "I feel sad sometimes, but it doesn't affect me much."
            3: Moderate sadness. The patient often feels sad, and it is somewhat noticeable.
                Example Response: "I feel sad often and it shows."
            4: Significant Sadness. The patient frequently feels sad, and it is noticeable.
                Example Response: "I feel sad most days, and people can tell."
            5: Severe sadness. The patient feels sad all the time and struggles to mask these feelings.
                Example Response: "I feel sad all the time and can't hide it."
            6: Extreme sadness. The patient is constantly overwhelmed by sadness, and it is clearly evident.
                Example Response: "I am always sad, and it's very obvious to everyone."
        """, 
    "example_conversation":"""
        Doctor: When you think about your recent emotions, do you find yourself feeling sad or down often?
        Patient: I've been feeling lazy and sad for the past two days
        Doctor: I'm sorry to hear that you've been feeling that way. Can you tell me more about what's been making you feel sad and lazy? Is there anything specific that's been weighing on your mind?
        Patient: I don't have any specific incident causing me to feel lazy and sad
        Doctor: I understand. Sometimes feelings of sadness and low energy can come without a specific cause. How has this been affecting your daily activities and interactions with others?
        Patient: It's affecting my daily work activities, and I'm unable to spend time with my family.
        Doctor: I'm sorry to hear that it's impacting your work and family time. It must be difficult to manage these feelings while trying to balance everything. Have you noticed if others around you have also noticed that you're feeling this way?
        Patient: Yes
        Doctor: It's tough when others notice that you're feeling this way. How have they been responding to your feelings of sadness and low energy?
        Patient: They haven't identified yet
        Doctor: I see. It's understandable that you may not want to worry them. However, it's essential to address these feelings to ensure you receive the support you need. Can you tell me more about what your feelings of sadness and low energy are like? How do they manifest throughout the day?
        Patient: The feeling of sadness recurs every two hours throughout the day
        Doctor: I appreciate you sharing that. It sounds like these feelings are quite persistent. When you experience these recurring feelings of sadness, do you notice any physical symptoms such as changes in appetite, sleep patterns, or energy levels?
        Patient: No
        Doctor: I understand. It's good to know that there haven't been significant changes in your physical well-being. Have you experienced these recurring feelings of sadness in the past, or is this the first time you've noticed them?
        Patient: I'm experiencing this for the first time
        Doctor: Thank you for sharing that. Experiencing these feelings for the first time can be unsettling. It's essential to address them and find ways to support you through this. Have you noticed any specific triggers or patterns that coincide with these recurring feelings of sadness?
        Patient: No
        Doctor: I appreciate your response. It's important to explore any potential triggers or patterns that may be contributing to these feelings. Understanding these factors can help in finding ways to manage and overcome these emotions. Is there anything else you'd like to share about how you've been feeling?
        Patient: No
        """,
    "example_rating":"""
        {"1": {"symptoms_identified":"Persistent sad, anxious, or empty or mood",
            "medical_key_points":"Duration,Impact,Mood",
            "rating":"6", "choice":"Very severe symptoms"},
        "2": {"symptoms_identified":"Persistent sad, anxious, or empty or mood",
            "medical_key_points":"Course,Impact,Mood", "rating":"6",
            "choice":"Very severe symptoms"},
        "3": {"symptoms_identified":"Persistent sad, anxious, or empty or mood",
            "medical_key_points":"Impact,Mood", "rating":"6",
            "choice":"Very severe symptoms"}, 
        "section_rating":{"rating":"6","choice":"Very severe symptoms"}
        }  
    """,
    "example_Symptems_key_points":""" 
        "Persistent sad, anxious, or empty or mood" : "Duration,Impact,Mood" 
        """ 
    },

"REDUCED_SLEEP":{
    "rating_guide_lines": """
        Reduced Sleeping Rating Guide:
        To assess reduced sleep, use the following scale based on patient responses:

            0: No sleep difficulties. The patient does not experience any reduction in sleep.
                Example Response: "I sleep the usual amount without any problems."
            1: Slightly reduced sleep. The patient sleeps up to 1 hour less than usual.
                Example Response: "I've been sleeping a bit less than usual, maybe up to an hour less."
            2: Mildly reduced sleep. The patient sleeps 1-2 hours less than usual.
                Example Response: "I've been sleeping a bit less than usual, maybe 1 or 2 hours less."
            3: Moderately reduced sleep. The patient sleeps 2-3 hours less than usual.
                Example Response: "My sleep has been reduced by 2 to 3 hours each night."
            4: Significantly reduced sleep. The patient sleeps 3-4 hours less than usual.
                Example Response: "I'm sleeping 3 to 4 hours less than I used to."
            5: Severely reduced sleep. The patient sleeps more than 4 hours less than usual.
                Example Response: "I'm sleeping over 4 hours less than I used to, and it's affecting me."
            6: Extremely reduced sleep. The patient has severe sleep deprivation, impacting daily life.
                Example Response: "I'm barely sleeping at all, and it's severely affecting me."
        """,
    "example_conversation":""" 
        Doctor: I understand that talking about sleep can be important. Let's discuss how you've been sleeping lately
        Patient: I have been sleeping poorly for the past week.
        Doctor: I'm sorry to hear that you've been having trouble sleeping. It can be really tough when sleep is disrupted. Can you tell me more about what's been making it difficult for you to sleep?
        Patient: I experienced some sleep disturbances due to stress
        Doctor: Stress can definitely have a big impact on sleep. It's completely understandable to have trouble sleeping when feeling stressed. Could you share more about the specific stressors that have been affecting your sleep?
        Patient: I believe the stress stems from work-related tasks at the office.
        Doctor: Work-related stress can be quite challenging to deal with. How has this stress been affecting your ability to fall asleep or stay asleep?
        Patient: I have not been sleeping well for almost every day in the last week
        Doctor: I understand, not being able to sleep well for several days can be really tough. On average, how many hours have you been managing to sleep each night during this time?
        Patient: It will be around 2 hours only
        Doctor: Thank you for sharing that. Getting only 2 hours of sleep a night is definitely concerning. I appreciate your openness in discussing this.
        """,
    "example_rating":"""  {"1": {"symptoms_identified":"Insomnia or poor sleep or oversleeping",
                                        "medical_key_points":"sleep,Course",
                                        "rating":"6",
                                        "choice":"Very severe symptoms"},
                            "2": {"symptoms_identified":"Insomnia or poor sleep or oversleeping",
                                        "medical_key_points":"sleep,Course",
                                        "rating":"6",
                                        "choice":"Very severe symptoms"},
                            "3": {"symptoms_identified":"Insomnia or poor sleep or oversleeping",
                                        "medical_key_points":"sleep,Course",
                                        "rating":"6",
                                        "choice":"Very severe symptoms"}, 
                            "section_rating":{"rating":"6","choice":"Very severe symptoms"}
                                                }  
                    """ ,
    "example_Symptems_key_points":""" 
        "Insomnia or poor sleep or oversleeping": "sleep,Course" 
        """
    },
"REDUCED_APPETITE":{
    "rating_guide_lines":"""
        Reduced Appetite Rating Guide:
        To assess reduced appetite, use the following scale based on patient responses:

            0: Normal appetite. The patient does not experience any reduction in appetite.
                Example Response: "My appetite is normal; I eat as usual."
            1: Slightly reduced appetite. The patient eats slightly less than usual.
                Example Response: "I've noticed that I'm eating a little less than usual."
            2: Mildly reduced appetite. The patient eats somewhat less than usual.
                Example Response: "I'm eating a bit less than I normally do."
            3: Moderately reduced appetite. The patient eats significantly less than usual.
                Example Response: "I've been eating much less than I normally do."
            4: Significantly reduced appetite. The patient eats very little compared to usual.
                Example Response: "My appetite is quite low; I'm eating much less."
            5: Severely reduced appetite. The patient has a very minimal appetite and eats very little.
                Example Response: "My appetite is almost gone; I'm barely eating anything."
            6: Extremely reduced appetite. The patient has almost no desire to eat and is significantly undernourished.
                Example Response: "I have no appetite at all; I struggle to eat anything."
        """,
    "example_conversation":""" 
        Doctor: Hello! I see that we're going to discuss reduced appetite today. I'm here to help you with any concerns you may have. Let's start by talking about your appetite. Have you noticed any changes in your appetite lately?
        Patient: Sometimes a eat less
        Doctor: I understand. It's important to pay attention to changes in appetite. Can you tell me more about when you started noticing this change?
        Patient: a couple of times a week
        Doctor: I see. When you do eat, do you feel full more quickly than usual?
        Patient: Yes
        Doctor: I understand. Have you experienced any unintentional weight loss recently?
        Patient: No
        Doctor: Thank you for sharing that. Have you noticed any changes in your sense of taste or smell that might be affecting your appetite?
        Patient: No
        Doctor: I appreciate your responses. It's important to consider various factors that might affect appetite. Have you been feeling more stressed or anxious lately, as these feelings can sometimes impact appetite?
        Patient: No
        I appreciate your input. Changes in appetite can be influenced by various factors, and it's important to explore them. Is there anything else you think might be contributing to your reduced appetite?
        Patient: No
        """,
    "example_rating":"""  {"1": {"symptoms_identified":"Changes in appetite and weight",
                                        "medical_key_points":"Appetite,Course",
                                        "rating":"2","choice":"Mild symptoms"},
                            "2": {"symptoms_identified":"Changes in appetite and weight",
                                        "medical_key_points":"Appetite,Course",
                                        "rating":"2","choice":"Mild symptoms"},
                            "3": {"symptoms_identified":"No symptoms identified",
                                        "medical_key_points":"Appetite",
                                        "rating":"0", "choice":"No symptoms"}, 
                            "section_rating":{"rating":"6","choice":"Very severe symptoms"}
                                }  
                    """,
    "example_Symptems_key_points":""" 
        "Changes in appetite and weight": "Appetite,Course" 
        """
    },
"REPORTED_SADNESS":{
    "rating_guide_lines": """
        Reported Sadness Rating Guide:
        To assess reported sadness, use the following scale based on patient responses:

            0: No sadness. The patient does not report feeling sad at all.
                Example Response: "I don't feel sad at all."
            1: Slight sadness. The patient rarely feels sad.
                Example Response: "I feel sad very occasionally."
            2: Mild sadness. The patient feels sad from time to time.
                Example Response: "I feel sad occasionally, but it's not frequent."
            3: Moderate sadness. The patient often feels sad.
                Example Response: "I feel sad quite often."
            4: Frequent sadness. The patient frequently feels sad.
                Example Response: "I feel sad most of the time."
            5: Severe sadness. The patient feels deeply sad almost all the time.
                Example Response: "I feel intensely sad nearly all the time."
            6: Extreme sadness. The patient feels overwhelmingly sad constantly.
                Example Response: "I feel overwhelmingly sad all the time."
        """,
    "example_conversation":""" 
        Doctor: I understand that talking about feelings of sadness can be difficult. Could you tell me how often you find yourself feeling sad or low?
        Patient: Im not feeling well for the past 10 days
        Doctor: I'm sorry to hear that you've been feeling this way for the past 10 days. On a scale from 0 to 10, with 0 being not intense at all and 10 being extremely intense, how intense would you say your feelings of sadness have been during this time?
        Patient: I would rate it a 9 out of 10.
        Doctor: I appreciate you sharing that with me. It sounds like these feelings have been quite intense. Are there particular things that tend to make you feel even sadder or more down during this time?
        Patient: Yes, these feelings are making me extremely sad.
        Doctor: I understand that these feelings are having a significant impact on you. Can you tell me more about the specific situations or thoughts that tend to make you feel even sadder?
        Patient: I don't have any specific situations that make me feel sad, but I think it is due to some financial issues in the family
        Doctor: I appreciate you sharing that with me. Financial issues can indeed be very stressful and can contribute to feelings of sadness. It's completely understandable to feel this way. Your feelings are valid, and I'm here to support you. If there's anything else you'd like to share about how these financial issues are affecting you, please feel free to do so.
        Patient: That is due to some recent business losses
        Doctor: I'm sorry to hear about the business losses. It's completely understandable that this situation would contribute to your feelings of sadness. If there's anything else you'd like to share about how these business losses are impacting you, please feel free to do so.
        Patient:No, Sorry
        """,
    "example_rating":"""  {"1": {"symptoms_identified":"Feelings of hopelessness or pessimism",
                                        "medical_key_points":"Mood,Duration",
                                        "rating":"6","choice":"Very severe symptoms"},
                            "2": {"symptoms_identified":"Feelings of hopelessness or pessimism",
                                "medical_key_points":"Mood,Duration",
                                "rating":"6","choice":"Very severe symptoms"},
                            "3": {"symptoms_identified":"No symptoms identified",
                                "medical_key_points":"Mood,Onset",
                                "rating":"6","choice":"Very severe symptoms"},
                            "section_rating":{"rating":"6","choice":"Very severe symptoms"}
                            }  
                    """,
    "example_Symptems_key_points":""" 
        "Feelings of hopelessness or pessimism": "Mood,Duration" 
        """
    },

"INNER_TENSION":{
    "rating_guide_lines":"""
        Inner Tension Rating Guide:
        To assess inner tension, use the following scale based on patient responses:

            0: No inner tension. The patient feels calm.
                Example Response: "I don't feel tense at all."
                1: Slight tension. The patient occasionally feels a bit tense.
            Example Response: "I feel a bit tense occasionally, but it's manageable."
            2: Mild tension. The patient sometimes feels tense.
                Example Response: "I feel tense sometimes, but it's not too bad."
            3: Moderate tension. The patient often feels tense and moderately anxious.
                Example Response: "I frequently feel tense and anxious."
            4: Frequent tension. The patient usually feels tense and anxious.
                Example Response: "I often feel tense and anxious."
            5: Severe tension. The patient feels tense most of the time with severe anxiety.
                Example Response: "I feel tense almost all the time and it's severe."
            6: Extreme tension. The patient constantly feels very tense and extremely anxious.
                Example Response: "I constantly feel extremely tense and anxious."
        """,
    "example_conversation":""" 
        Doctor: Hello! I understand that inner tension and restlessness can be quite challenging. I'm here to listen and help you through this. Can you share with me what it's like for you when you experience inner tension?
        Patient: I feel inner tension when I meet new people and start conversations
        Doctor: I understand that meeting new people and starting conversations can be a source of inner tension for many. It's completely normal to feel that way. Can you tell me more about how this inner tension manifests for you in those situations?
        Patient: I feel very anxious or tense inside, but I appear calm at that time
        Doctor: It sounds like you're able to keep a calm exterior even when you're feeling anxious or tense inside. That can be quite challenging. How do you usually cope with these feelings when you're in those situations?
        Patient: Nothing, I remain calm at that time.
        Doctor: I see. It's interesting that you're able to maintain a calm demeanor despite feeling anxious inside. Have you noticed any physical symptoms accompanying this inner tension, such as increased heart rate or sweating?
        Patient: I start sweating at that moment
        Doctor: Thank you for sharing that. Sweating can be a common physical response to inner tension. Have you found any strategies that help you manage this sweating when you're in those situations?
        Patient: No
        Doctor: I appreciate your honesty. It's not always easy to find strategies to manage these physical responses. Have you noticed if this sweating has caused any additional discomfort or concerns for you in social situations?
        Patient:No
        """,
    "example_rating":"""  {"1": {"symptoms_identified":"Feelings of anxiety, nervousness, or inner tension",
                                        "medical_key_points":"Tension,Duration",
                                    "rating":"2","choice":"Mild symptoms"},
                            "2": {"symptoms_identified":"Feelings of anxiety, nervousness, or inner tension",
                                "medical_key_points":"Tension,Impact,Duration",
                                "rating":"6","choice":"Very severe symptoms"},
                            "3": {"symptoms_identified":"Feelings of anxiety, nervousness, or inner tension",
                                "medical_key_points":"Tension",
                                "rating":"6","choice":"Very severe symptoms"},
                            "section_rating":{"rating":"6","choice":"Very severe symptoms"}
                            }  
                    """,
    "example_Symptems_key_points":"""
        "Feelings of anxiety, nervousness, or inner tension": "Tension,Impact,Duration"
        """
},

"CONCENTRATION_DIFFICULTIES":{
    "rating_guide_lines":"""
        Concentration Difficulties Rating Guide:
        To assess concentration difficulties, use the following scale based on patient responses:

            0: No concentration difficulties. The patient can focus normally.
                Example Response: "I don't have any trouble concentrating."
            1: Slight concentration difficulties. The patient rarely has trouble focusing.
                Example Response: "I occasionally have slight trouble concentrating."
            2: Mild concentration difficulties. The patient sometimes has difficulty focusing.
                Example Response: "I sometimes have trouble concentrating."
            3: Moderate concentration difficulties. The patient often finds it hard to focus.
                Example Response: "I frequently have trouble concentrating on tasks."
            4: Frequent concentration difficulties. The patient usually has significant trouble focusing.
                Example Response: "I usually have significant trouble concentrating."
            5: Severe concentration difficulties. The patient constantly has difficulty focusing.
                Example Response: "I constantly have trouble concentrating, no matter what I'm doing."
            6: Extreme concentration difficulties. The patient is almost unable to focus at all.
                Example Response: "I am almost unable to concentrate at all, no matter what I'm doing."
        """,
    "example_conversation": """ 
        Doctor: Could you share a recent situation where you found it hard to concentrate?
        Patient: There was a situation in recent times where I could not concentrate on my business meeting due to overwhelming stress and anxiety
        Doctor:I understand that feeling stressed and anxious can really impact your ability to concentrate. It sounds like it was a challenging experience. Can you tell me more about what specifically was causing the stress and anxiety during the meeting? 
        Patient: Maybe that is due to a lack of business knowledge
        Doctor: I appreciate you sharing that. Feeling overwhelmed by a lack of business knowledge can definitely contribute to stress and anxiety. It's completely understandable to feel that way. Can you tell me more about the specific aspects of the business meeting that made you feel this way?
        Patient: Nothing specific
        Doctor: I see. It's okay if you don't have specific details to share. It's common to feel overwhelmed in situations like business meetings. Have you noticed this difficulty in concentration happening in other areas of your life as well, or is it mostly related to work-related situations?
        Patient: Sometimes it happens in other areas of my life as well
        Doctor: I appreciate you sharing that. It's important to understand how concentration difficulties may be affecting different aspects of your life. Can you provide an example of a situation outside of work where you've experienced difficulty concentrating?
        Patient: One example is during family dinners; I find it hard to stay focused on conversations. My mind often drifts, and I struggle to keep up with what everyone is saying.
        Doctor: Thank you for sharing that. It can be really challenging when you're unable to fully engage in conversations, especially during family time. Have you noticed any specific triggers or patterns that seem to lead to these difficulties in focusing during family dinners?
        Patient:No
        """,
    "example_rating":"""  {"1": {"symptoms_identified":"Difficulty concentrating, remembering, or making decisions",
                                "medical_key_points":"Cognitive,Impact",
                                "rating":"6","choice":"Very severe symptoms"},
                            "2": {"symptoms_identified":"Difficulty concentrating, remembering, or making decisions",
                                "medical_key_points":"Cognitive,Impact",
                                "rating":"6","choice":"Very severe symptoms"},
                            "3": {"symptoms_identified":"Difficulty concentrating, remembering, or making decisions",
                                "medical_key_points":"Cognitive,Impact",
                                "rating":"6","choice":"Very severe symptoms"},
                            "section_rating":{"rating":"6","choice":"Very severe symptoms"}
                            }  
                        """,
    "example_Symptems_key_points":""" 
        "Difficulty concentrating, remembering, or making decisions":"Cognitive,Impact"
        """
    },

"LASSITUDE":{
    "rating_guide_lines":"""
        Lassitude Rating Guide:
        To assess lassitude, use the following scale based on patient responses:

            0: No lassitude. The patient feels energetic.
                Example Response: "I feel energetic and don't experience tiredness."
            1: Slight lassitude. The patient occasionally feels slightly tired.
                Example Response: "I occasionally feel a bit tired."
            2: Mild lassitude. The patient sometimes feels tired or listless.
                Example Response: "I sometimes feel tired or listless."
            3: Moderate lassitude. The patient often feels tired or listless.
                Example Response: "I frequently feel tired and listless."
            4: Frequent lassitude. The patient usually feels tired and listless.
                Example Response: "I usually feel tired and listless."
            5: Severe lassitude. The patient constantly feels tired or listless.
                Example Response: "I constantly feel tired and listless, no matter what I do."
            6: Extreme lassitude. The patient feels extremely tired and listless all the time.
                Example Response: "I feel extremely tired and listless all the time, and it's very overwhelming."
        """,
    "example_conversation": """ 
        Doctor: I understand that discussing health concerns can sometimes feel overwhelming. Your well-being is important, and I'm here to help you through it. Now, let's talk about lassitude. Do you often feel physically and mentally exhausted?
        Patient: Yes, most of the time I feel physically and mentally exhausted
        Doctor:I appreciate you sharing that with me. It's important to address these feelings of exhaustion. Can you tell me more about how frequently you experience these feelings of fatigue or lethargy? 
        Patient: almost every day
        Doctor: I see, feeling fatigued on a daily basis can be quite challenging. Have you noticed any activities that used to give you energy but now don't seem to have the same effect?
        Patient: Walking was one of the activity mostly I used to do that gives me energy but currently it is not
        Doctor: Walking was one of the activity mostly I used to do that gives me energy but currently it is not
        Patient: Okay
        Doctor: I understand. It's important to gather detailed information to better understand your situation. Can you tell me more about how this change in your energy levels has affected your daily life and activities?
        Patient: It's affecting almost all of my daily activities
        Doctor: I appreciate you sharing that with me. It must be quite challenging to navigate through your daily activities feeling this way. Can you provide some specific examples of how it's impacting your daily life?
        Patient:I was not able to move actively and feeling tired all the time
        Doctor:I understand how difficult that must be for you. Feeling tired all the time and being unable to move actively can significantly impact your daily life. Thank you for sharing this information with me. This will help in understanding your situation better.
        Patient:Okay
        """,
    "example_rating":"""  {"1": {"symptoms_identified":"Fatigue and decreased energy",
                                "medical_key_points":"Energy,Duration",
                                "rating":"6","choice":"Very severe symptoms"},
                            "2":{"symptoms_identified":"Fatigue and decreased energy",
                                "medical_key_points":"Energy,Duration",
                                "rating":"6","choice":"Very severe symptoms"},
                            "3": {"symptoms_identified":"Fatigue and decreased energy",
                                "medical_key_points":"Energy,Duration,Impact",
                                "rating":"6","choice":"Very severe symptoms"},
                            "section_rating":{"rating":"6","choice":"Very severe symptoms"}
                        }  
                    """,
    "example_Symptems_key_points": """ 
        "Fatigue and decreased energy":"Energy,Duration,Impact"
        """    
    },

"INABILITY_TO_FEEL":{
    "rating_guide_lines":"""
        Inability to Feel Rating Guide:
        To assess inability to feel, use the following scale based on patient responses:

            0: No difficulties in experiencing emotions. The patient feels normal emotions.
                Example Response: "I experience emotions normally."
            1: Slight difficulty in feeling emotions. The patient occasionally feels slightly emotionally numb.
                Example Response: "I occasionally feel a bit emotionally numb."
            2: Mild difficulty in feeling emotions. The patient sometimes feels emotionally numb.
                Example Response: "I sometimes feel emotionally numb."
            3: Moderate difficulty in feeling emotions. The patient often feels emotionally numb.
                Example Response: "I frequently feel emotionally numb."
            4: Frequent difficulty in feeling emotions. The patient usually feels emotionally numb.
                Example Response: "I usually feel emotionally numb."
            5: Severe difficulty in feeling emotions. The patient constantly feels emotionally numb.
                Example Response: "I constantly feel emotionally numb and detached."
            6: Extreme difficulty in feeling emotions. The patient feels completely emotionally numb all the time.
                Example Response: "I feel completely emotionally numb all the time, and it's very distressing."
        """,
    "example_conversation":""" 
        Doctor:Could you describe what it's like for you when you feel emotionally numb? 
        Patient: When I feel emotionally numb, it's like a void where I can't connect with any feelings, positive or negative. It's a sense of emptiness that makes it hard to engage with anything around me
        Doctor: It sounds like feeling emotionally numb creates a sense of disconnection and emptiness for you. That must be quite challenging. Can you think of any specific situations or triggers that seem to bring about this feeling of emotional numbness for you?
        Patient: One specific situation that brings about this feeling is when I'm under a lot of stress at work. Deadlines and high expectations often make me shut down emotionally
        Doctor: It's understandable that high levels of stress at work can trigger this emotional numbness for you. That sounds like a tough situation to navigate. How do you usually cope with these feelings when they arise?
        Patient: I usually cope by taking short breaks throughout the day and practicing deep breathing exercises to help me relax
        Doctor: It's great to hear that you have strategies in place to help manage these feelings. Taking breaks and practicing deep breathing can be really effective ways to alleviate stress. Have you noticed any other changes in your life or behavior that seem to coincide with these periods of emotional numbness?
        Patient: No
        Doctor: I appreciate your openness in sharing your experiences. Understanding the impact of emotional numbness on your daily life is important. Have you noticed any changes in your ability to feel pleasure or enjoyment in activities you once loved?
        Patient: Yes, I struggle to find pleasure or enjoyment in activities I once loved. Even things that used to make me happy now feel uninteresting and dull
        Doctor: It's tough when activities that once brought joy now feel uninteresting. I can imagine how disheartening that must be. Is there anything else you'd like to share about how this has been affecting you?
        Patient: No
        """,
    "example_rating":"""  {"1": {"symptoms_identified":"Loss of interest in activities once enjoyed",
                                "medical_key_points":"Anhedonia,Impact",
                                "rating":"6","choice":"Very severe symptoms"},
                            "2":{"symptoms_identified":"Loss of interest in activities once enjoyed",
                                "medical_key_points":"Anhedonia,Onset",
                                "rating":"6","choice":"Very severe symptoms"},
                            "3": {"symptoms_identified":"Loss of interest in activities once enjoyed",
                                "medical_key_points":"Anhedonia",
                                "rating":"6","choice":"Very severe symptoms},
                            "section_rating":{"rating":"6","choice":"Very severe symptoms"}
                        }  
        """,
    "example_Symptems_key_points":""" 
        "Loss of interest in activities once enjoyed":"Anhedonia"
        """   
    },
"PESSIMISTIC_THOUGHTS":{
    "rating_guide_lines": """
        Pessimistic Thoughts Rating Guide:
        To assess pessimistic thoughts, use the following scale based on patient responses:

            0: No pessimistic thoughts. The patient is generally optimistic.
                Example Response: "I don't have any pessimistic thoughts."
            1: Slight pessimistic thoughts. The patient rarely has negative thoughts.
                Example Response: "I rarely have pessimistic thoughts."
            2: Mild pessimistic thoughts. The patient sometimes has negative thoughts.
                Example Response: "I occasionally have pessimistic thoughts."
            3: Moderate pessimistic thoughts. The patient often has negative thoughts.
                Example Response: "I frequently have pessimistic thoughts."
            4: Frequent pessimistic thoughts. The patient usually has negative thoughts.
                Example Response: "I usually have pessimistic thoughts."
            5: Severe pessimistic thoughts. The patient constantly has negative thoughts.
                Example Response: "I constantly have pessimistic thoughts and feel hopeless."
            6: Extreme pessimistic thoughts. The patient is overwhelmingly pessimistic all the time.
                Example Response: "I feel overwhelmingly pessimistic all the time, and it feels hopeless."
        """,
    "example_conversation":""" 
        Doctor: Could you share some recent situations that have triggered these pessimistic thoughts?
        Patient:Recent setbacks in my projects and conflicts with colleagues have triggered pessimistic thoughts 
        Doctor: I understand how setbacks and conflicts can be really disheartening. It's completely normal to feel pessimistic in such situations. If it's okay with you, I'd like to understand a bit more about how these setbacks and conflicts have been affecting you. Can you tell me more about the specific thoughts or feelings that have been coming up for you as a result of these situations?
        Patient:"I've been feeling overwhelmed and doubting my abilities due to these setbacks and conflicts. 
        Doctor: It sounds like these experiences have been really tough on you. It's completely understandable to feel overwhelmed and doubt your abilities when facing such challenges. I'm here to listen and support you as you navigate through these feelings. Is there anything else you'd like to share about how these thoughts have been affecting you?
        Patient: Yes, it's been difficult, and I appreciate your support. These thoughts have been affecting my confidence and making it hard to focus on my task
        Doctor: I'm glad that you feel comfortable sharing with me, and I want you to know that you're not alone in feeling this way. It's completely valid to have your confidence shaken by these experiences. I appreciate your openness, and I'm here to help you work through these challenges. Is there anything specific that you find particularly challenging when it comes to focusing on your tasks?
        Patient: One challenge I face is maintaining focus amidst distractions.
        Doctor:I understand how distractions can make it even more difficult to focus, especially when you're already feeling overwhelmed. Have you found any strategies or techniques that have helped you manage these distractions in the past, or are there specific areas where you find it most challenging to stay focused? 
        Patient: Yes, I've found that setting specific time blocks and minimizing interruptions help me stay focused
        Doctor: That's a great approach! Setting specific time blocks and minimizing interruptions can be really effective in maintaining focus. It's wonderful that you've found a strategy that works for you. Is there anything else you'd like to share about how you've been managing these challenges, or any other aspects of these pessimistic thoughts that you'd like to discuss?
        Patient: No
        """,
    "example_rating":"""  {"1": {"symptoms_identified":"Feelings of hopelessness or pessimism,shows little optimism",
                                "medical_key_points":"Mood,Impact,Pessimism",
                                "rating":"6","choice":"Very severe symptoms"},
                            "2":{"symptoms_identified":"Feelings of hopelessness or pessimism,shows little optimism",
                                "medical_key_points":"Mood,Pessimism,Duration",
                                "rating":"6","choice":"Very severe symptoms"},
                            "3": {"symptoms_identified":"Feelings of hopelessness or pessimism,shows little optimism",
                                "medical_key_points":"Mood,Pessimism",
                                "rating":"6","choice":"Very severe symptoms"},
                            "section_rating":{"rating":"6","choice":"Very severe symptoms"}
                         }  
                    """,
    "example_Symptems_key_points":""" 
        "Feelings of hopelessness or pessimism,shows little optimism":"Mood,Pessimism"
        """
    },
        
"SUICIDAL_THOUGHTS":{
    "rating_guide_lines":"""
        Suicidal Thoughts Rating Guide:
        To assess suicidal thoughts, use the following scale based on patient responses:

        0: No suicidal thoughts. The patient does not think about self-harm.
            Example Response: "I don't have any thoughts about hurting myself."
        1: Slight suicidal thoughts. The patient rarely thinks about self-harm.
            Example Response: "I rarely have thoughts about hurting myself."
        2: Mild suicidal thoughts. The patient sometimes thinks about self-harm.
            Example Response: "I occasionally have thoughts about hurting myself."
        3: Moderate suicidal thoughts. The patient often thinks about self-harm.
            Example Response: "I frequently have thoughts about hurting myself."
        4: Frequent suicidal thoughts. The patient usually thinks about self-harm.
            Example Response: "I usually have thoughts about hurting myself."
        5: Severe suicidal thoughts. The patient constantly thinks about self-harm or has made preparations.
            Example Response: "I constantly have thoughts about hurting myself and have even made plans."
        6: Extreme suicidal thoughts. The patient has made detailed plans or attempts at self-harm.
            Example Response: "I have made detailed plans to hurt myself and think about it all the time."
    """,
    "example_conversation":""" 
        Doctor: I understand that discussing this topic can be sensitive, but it's important. Your well-being is my priority. Let's take this one step at a time. Can you share with me if you've had any thoughts about hurting yourself or ending your life recently?
        Patient:Yes, I had thoughts about hurting myself and ending my life when I was feeling very low after my father passed away 
        Doctor: Losing a loved one can be incredibly difficult, and it's understandable to feel overwhelmed during such a challenging time. I'm here to listen and support you. Can you tell me more about these thoughts and how often you've been experiencing them since your father passed away?
        Patient: only once
        Doctor: I appreciate you sharing that with me. It's important to address these thoughts, even if they've only occurred once. Do you have any specific plans for harming yourself?
        Patient: No, I don't have any specific plans for harming yourself?
        Doctor: I'm glad to hear that you don't have any specific plans. It's important to address these thoughts and feelings to ensure your well-being. Can you tell me more about what has been helping you cope with these thoughts since your father's passing?
        Patient:I have been doing yoga daily, and it has been helping me cope with these thoughts since my father's passing 
        Doctor: It's great to hear that yoga has been a positive outlet for you during this challenging time. Finding healthy ways to cope is important, and it's wonderful that you've found something that brings you comfort. Is there anything else that has been particularly helpful for you in managing these difficult emotions?
        Patient: No
        Doctor: Thank you for sharing that with me. It's important to acknowledge the progress you've made in finding healthy coping mechanisms. If you ever feel overwhelmed or these thoughts resurface, remember that support is available. Is there anything else you'd like to discuss about this or any other concerns you have?
        Patient: No
        """,
    "example_rating":"""  {"1": {"symptoms_identified":"Thoughts of death or suicide",
                                "medical_key_points":"Suicidal Ideation,Onset",
                                "rating":"2","choice":"Mild symptoms"},
                            "2":{"symptoms_identified":"Thoughts of death or suicide",
                                "medical_key_points":"Suicidal Ideation,Onset,Course",
                                "rating":"2","choice":"Mild symptoms"},
                            "3": {"symptoms_identified":"Thoughts of death or suicide",
                                "medical_key_points":"Suicidal Ideation",
                                "rating":"2","choice":"Mild symptoms"},
                            "section_rating":{"rating":"2","choice":"Mild symptoms"}
                            }  
                        """,
    "example_Symptems_key_points":""" 
        "Thoughts of death or suicide":"Suicidal Ideation,Onset"
        """
    }
}