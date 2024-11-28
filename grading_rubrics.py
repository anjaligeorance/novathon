import llmware

# Define grading logic
def calculate_similarity(student_answer, ideal_answer):
    """
    Use LLMWare's semantic similarity API to calculate similarity score.
    :param student_answer: Text extracted from the student's submission
    :param ideal_answer: Ideal answer for comparison
    :return: Similarity score (0 to 100)
    """
    try:
        score = llmware.semantic_similarity(student_answer, ideal_answer) * 100
        return score
    except Exception as e:
        print(f"Error using LLMWare Semantic Similarity: {e}")
        return 0

def grade_submission(student_text, rubric):
    """
    Grade the submission based on a rubric.
    :param student_text: Text extracted from the student's submission
    :param rubric: List of dictionaries containing 'question' and 'ideal_answer'
    :return: Graded result
    """
    results = []
    for question in rubric:
        question_text = question['question']
        ideal_answer = question['ideal_answer']
        score = calculate_similarity(student_text, ideal_answer)
        results.append({
            'question': question_text,
            'score': score,
            'feedback': "Excellent" if score > 90 else "Good" if score > 75 else "Needs Improvement"
        })
    return results
