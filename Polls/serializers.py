from rest_framework import serializers

from Polls.models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'votes')


class PollsSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'timestamp', 'choices')

    # def update(self, validated_data):
    #     choices_data = validated_data.pop('choices')
    #     question = Question.objects.create(**validated_data)
    #     for choice_data in choices_data:
    #         Choice.objects.create(question=question, **choices_data)
    #     return question
