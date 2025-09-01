import pandas as pd

def fetch_unique_answers(cursor):
    """
    Fetch questions with more than 5 distinct answers and display in a DataFrame.
    """
    rows = cursor.execute(
        """
        SELECT questionid, COUNT(DISTINCT answertext) AS unique_answers
        FROM answer
        GROUP BY questionid
        HAVING COUNT(DISTINCT answertext) > 5
        ORDER BY unique_answers DESC;
        """
    ).fetchall()
    
    df = pd.DataFrame(rows, columns=[description[0] for description in cursor.description])
    print(df)



def pivot_qualitative_answers(cursor):
    """
    Fetch answers for questions with more than 12 distinct answers and pivot them for display.
    """
    rows = cursor.execute(
        """
        WITH QualitativeQuestions AS (
        SELECT questionid
        FROM answer
        GROUP BY questionid
        HAVING COUNT(DISTINCT answertext) > 12
        )
        SELECT a.questionid, a.answertext
        FROM answer a
        JOIN QualitativeQuestions q ON a.questionid = q.questionid;
        """
    ).fetchall()

    df_quali = pd.DataFrame(rows, columns=[description[0] for description in cursor.description])
    df_quali['row_num'] = df_quali.groupby('QuestionID').cumcount() + 1

    df_pivot = df_quali.pivot(index='row_num', columns='QuestionID', values='AnswerText')
    df_pivot.reset_index(drop=True, inplace=True)
    print(df_pivot)



def pivot_avg_length_answers(cursor):
    """
    Fetch answers for questions where the average length of the answers is more than 20 characters, and pivot them.
    """
    rows = cursor.execute(
        """
        WITH QualitativeQuestions AS (
        SELECT questionid
        FROM answer
        GROUP BY questionid
        HAVING AVG(LENGTH(answertext)) > 20
        )
        SELECT a.questionid, a.answertext
        FROM answer a
        JOIN QualitativeQuestions q ON a.questionid = q.questionid;
        """
    ).fetchall()

    df_quali = pd.DataFrame(rows, columns=[description[0] for description in cursor.description])
    df_quali['row_num'] = df_quali.groupby('QuestionID').cumcount() + 1

    df_pivot = df_quali.pivot(index='row_num', columns='QuestionID', values='AnswerText')
    df_pivot.reset_index(drop=True, inplace=True)
    print(df_pivot)