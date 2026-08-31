MAX_RENTAL_BATCH_LIMIT = 150.0

def calculate_rental_batch (quantity: int, rental_rate: float, discount: float= 0.0) -> tuple[float,bool]:
    """
    This function calculates the rental batch sum and finds out limit exceedance

    Args:
        quantity (int): quantity of rental batch
        rental_rate (float): rate of rental batch

    Returns:
        tuple[float,bool]: sum of batch and result of limit exceedance
    """
    final_sum = quantity * rental_rate * (1 - discount)
    is_limit_exeeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return final_sum, is_limit_exeeded


batch1_sum, batch1_result = calculate_rental_batch(quantity=30, rental_rate=2.99)
batch2_sum, batch2_result = calculate_rental_batch(discount=0.1, quantity=40, rental_rate=4.99)
batch3_sum, batch3_result = calculate_rental_batch(10, 1.99)
batch4_sum, batch4_result = calculate_rental_batch(50, 3.50, 0.2)

print(f"batch 1 (Academy Dinosaur): sum {batch1_sum:.2f}. limit exceedance: {batch1_result}")

print(f"batch 2 (Affair Prejudice): sum {batch2_sum:.2f}. limit exceedance: {batch2_result}")

print(f"batch 3 (Agent Truman): sum {batch3_sum:.2f}. limit exceedance: {batch3_result}")

print(f"batch 4 (African Egg): sum {batch4_sum:.2f}. limit exceedance: {batch4_result}")
