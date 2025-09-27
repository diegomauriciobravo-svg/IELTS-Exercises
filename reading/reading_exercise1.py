# reading/reading_exercise1.py

def main():
    passage = """
Climate change is one of the most pressing issues of the 21st century. 
Scientists agree that rising global temperatures are largely due to human 
activities such as burning fossil fuels, deforestation, and intensive agriculture. 
These activities release greenhouse gases, primarily carbon dioxide and methane, 
which trap heat in the atmosphere. 

The consequences are significant: melting ice caps, rising sea levels, and 
increasingly severe weather events such as hurricanes, droughts, and floods. 
Beyond environmental impacts, climate change also threatens food security, 
public health, and economic stability. 

International organizations, including the United Nations, have called for urgent 
global cooperation. The Paris Agreement of 2015 represents a major step in 
encouraging nations to reduce emissions and transition to renewable energy. 
However, progress has been uneven, and many experts argue that stronger action 
is required to limit warming to 1.5°C above pre-industrial levels. 

Ultimately, addressing climate change requires both systemic policy changes and 
individual efforts. Governments, industries, and citizens must all play a role in 
shaping a sustainable future.
"""

    questions = [
        {
            "q": "1. What is identified as the primary cause of rising global temperatures?",
            "options": ["A. Natural cycles", "B. Human activities", "C. Ocean currents", "D. Solar flares"],
            "answer": "B"
        },
        {
            "q": "2. Which gases are mainly responsible for trapping heat in the atmosphere?",
            "options": ["A. Oxygen and nitrogen", "B. Hydrogen and helium", "C. Carbon dioxide and methane", "D. Ozone and argon"],
            "answer": "C"
        },
        {
            "q": "3. Which of the following is NOT mentioned as a consequence of climate change?",
            "options": ["A. Rising sea levels", "B. Increased volcanic activity", "C. Severe weather events", "D. Melting ice caps"],
            "answer": "B"
        },
        {
            "q": "4. What global agreement in 2015 aimed to address climate change?",
            "options": ["A. The Kyoto Protocol", "B. The Paris Agreement", "C. The Rio Summit", "D. The Montreal Protocol"],
            "answer": "B"
        },
        {
            "q": "5. What temperature increase are experts trying to limit warming to?",
            "options": ["A. 3°C", "B. 2°C", "C. 1.5°C", "D. 0.5°C"],
            "answer": "C"
        },
        {
            "q": "6. Which of the following is a potential impact of climate change mentioned in the passage?",
            "options": ["A. Economic instability", "B. Decreased literacy rates", "C. Population growth", "D. Decline in technology"],
            "answer": "A"
        },
        {
            "q": "7. According to the passage, what must nations transition towards?",
            "options": ["A. More deforestation", "B. Renewable energy", "C. Nuclear weapons", "D. Larger cities"],
            "answer": "B"
        },
        {
            "q": "8. Which international organization is mentioned as calling for cooperation?",
            "options": ["A. NATO", "B. The European Union", "C. The United Nations", "D. The World Bank"],
            "answer": "C"
        },
        {
            "q": "9. What role do individuals play in addressing climate change?",
            "options": ["A. None, it is only for governments", "B. They must relocate to colder areas", "C. They must consume more fossil fuels", "D. They must contribute to shaping a sustainable future"],
            "answer": "D"
        },
        {
            "q": "10. Which statement best summarizes the main idea of the passage?",
            "options": ["A. Climate change is caused by solar flares", "B. Climate change is not a global issue", 
                        "C. Climate change requires urgent and collective action", "D. Climate change has no economic impact"],
            "answer": "C"
        }
    ]

    print("=== IELTS Reading Passage ===\n")
    print(passage)
    print("=== Questions ===\n")

    score = 0
    for q in questions:
        print(q["q"])
        for opt in q["options"]:
            print(opt)
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        if ans == q["answer"]:
            score += 1
        print()

    print("=== Results ===")
    print(f"You scored {score} out of {len(questions)}")
    print("\nCorrect answers:")
    for q in questions:
        print(f"{q['q']} Correct: {q['answer']}")

if __name__ == "__main__":
    main()
