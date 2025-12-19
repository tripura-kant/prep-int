with open("ec2.log") as f:
    for line in f:
        instance_id = line.strip()

        print(
            f"aws ec2 describe-instance-status --instance-ids {instance_id}"
        )