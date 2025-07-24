class LowCreditScoreError(Exception):
    pass

def check_loan_eligibility():
    try:
        income = float(input("Enter annual income: "))
        assert income > 0, "Income must be positive"
        
        credit_score = int(input("Enter credit score (300-850): "))
        if credit_score < 300 or credit_score > 850:
            raise ValueError("Credit score must be between 300 and 850")
            
        if credit_score < 600:
            raise LowCreditScoreError("Credit score too low for loan")
            
        if income >= 50000 and credit_score >= 700:
            print("Approved for premium loan!")
        elif income >= 30000 and credit_score >= 600:
            print("Approved for standard loan")
        else:
            print("Approved for basic loan")
            
    except (ValueError, AssertionError, LowCreditScoreError) as e:
        print(f"Error: {e}")
    else:
        print("Application processed successfully")
    finally:
        print("Thank you for applying")

check_loan_eligibility()