# Simple CLI Quiz App
def main():
	questions = [
		{
			"question": "What is the smallest prime number?",
			"choices": ["Two", "One", "Three", "Five", "Zero"],
			"answer": 1  # Indexing from 1
		},
		{
			"question": "Which number is an even prime number?",
			"choices": ["Two", "Four", "Six", "Eight", "Ten"],
			"answer": 1
		},
		{
			"question": "What is the value of pi (π) rounded to two decimal places?",
			"choices": ["3.12", "3.14", "3.15", "3.16", "3.13"],
			"answer": 2
		},
		{
			"question": "Which of the following is NOT a prime number?",
			"choices": ["2", "3", "5", "9", "7"],
			"answer": 4
		},
		{
			"question": "What is the next prime number after 7?",
			"choices": ["9", "10", "11", "12", "13"],
			"answer": 3
		}
	]

	score = 0
	for idx, q in enumerate(questions, 1):
		print(f"\nQuestion {idx}: {q['question']}")
		for i, choice in enumerate(q['choices'], 1):
			print(f"  {i}. {choice}")
		try:
			user_ans = int(input("Your answer (1-5): "))
		except ValueError:
			user_ans = 0
		if user_ans == q['answer']:
			print("Correct!")
			score += 1
		else:
			print(f"Incorrect. The correct answer is {q['answer']}: {q['choices'][q['answer']-1]}")

	print(f"\nQuiz complete! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
	main()
