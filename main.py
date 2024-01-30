import os

from boto3 import Session

profile_name = os.getenv("PROFILE_NAME") or "default"
region_name = os.getenv("REGION_NAME") or "us-east-1"
ecs_cluster_name = os.getenv("CLUSTER_NAME") or "default"

ecs_service_name = os.getenv("SERVICE_NAME")

session = Session(profile_name=profile_name, region_name=region_name)
ecs_client = session.client("ecs")


def get_running_count(ecs_client, ecs_cluster_name, ecs_service_name):
	service = ecs_client.describe_services(
		cluster=ecs_cluster_name,
		services=[ecs_service_name]
	)
	return service["services"][0]["runningCount"]


def set_task_count(ecs_client, ecs_cluster_name, ecs_service_name, count):
	ecs_client.update_service(cluster=ecs_cluster_name,
	                          service=ecs_service_name,
	                          desiredCount=count)
	waiter = ecs_client.get_waiter('services_stable')
	waiter.wait(
		cluster=ecs_cluster_name,
		services=[
			ecs_service_name,
		],
		WaiterConfig={
			'MaxAttempts': 999
		}
	)


if __name__ == '__main__':
	running_count = get_running_count(ecs_client, ecs_cluster_name, ecs_service_name)
	count = 0
	print(f"Changing service {ecs_service_name} to the desired count of {count}")
	set_task_count(ecs_client=ecs_client, ecs_cluster_name=ecs_cluster_name, ecs_service_name=ecs_service_name,
	               count=count)
	print(f"Changing service {ecs_service_name} to the desired count of {running_count}")
	set_task_count(ecs_client=ecs_client, ecs_cluster_name=ecs_cluster_name, ecs_service_name=ecs_service_name,
	               count=running_count)
