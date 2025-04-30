def get_coupon():
    try:
        coupon = float(input("Enter the coupon amount as a decimal (e.g., 0.10 for 10%): "))
        if coupon <= 0 or coupon > 1:
            print("Invalid coupon value. Defaulting to 10% discount.")
            return 0.10
        return coupon
    except ValueError:
        print("Invalid input. Defaulting to 10% discount.")
        return 0.10

def get_weekly_bills():
    weekly_bills = []
    for i in range(1, 5):
        while True:
            try:
                bill = float(input(f"Enter grocery bill for week {i}: $"))
                if bill < 0:
                    print("Bill cannot be negative. Try again.")
                    continue
                weekly_bills.append(bill)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return weekly_bills

def main():
    coupon = get_coupon()
    weekly_bills = get_weekly_bills()

    monthly_total = sum(weekly_bills)
    weekly_avg = monthly_total / 4

    monthly_total_discounted = monthly_total * (1 - coupon)
    weekly_avg_discounted = monthly_total_discounted / 4

    print("\n--- Results ---")
    print(f"Monthly Total (no coupon): ${monthly_total:.2f}")
    print(f"Weekly Average (no coupon): ${weekly_avg:.2f}")
    print(f"Monthly Total (with coupon): ${monthly_total_discounted:.2f}")
    print(f"Weekly Average (with coupon): ${weekly_avg_discounted:.2f}")

if __name__ == "__main__":
    main()
