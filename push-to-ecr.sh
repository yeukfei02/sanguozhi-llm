#! /bin/zsh

source .env

echo "AWS_ACCOUNT_ID = $AWS_ACCOUNT_ID"

if [ ! -z "$AWS_ACCOUNT_ID" ]; then
    AWS_ACCOUNT_ID="$AWS_ACCOUNT_ID"
    AWS_REGION="ap-southeast-1"
    IMAGE_NAME="sanguozhi-llm-api"
    ECR_REPOSITORY="sanguozhi-llm-api"
    TAG="latest"

    # build docker image
    docker build -t $IMAGE_NAME .

    # login to aws ecr
    aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

    # docker tag
    docker tag $IMAGE_NAME:$TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY:$TAG

    # push to ecr
    docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY:$TAG
fi
