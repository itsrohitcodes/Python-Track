# Build a Training Batch Tracker using Class Variables

class TrainingBatch:
    # Add class variables here
    platform_name = "KodNest"
    batch_count = 0

    def __init__(self, batch_name):
        # Store the batch name and update the counter
        self.batch_name = batch_name

        TrainingBatch.batch_count += 1


n = int(input())
batches = []

for _ in range(n):
    batch_name = input().strip()
    batches.append(TrainingBatch(batch_name))

for batch in batches:
    print(f"{TrainingBatch.platform_name} - {batch.batch_name}")

print(f"Total Batches: {TrainingBatch.batch_count}")