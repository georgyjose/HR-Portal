from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TimeSlot
from .serializers import TimeSlotSerializer
from datetime import timedelta


class InterviewerList(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer


class TimeSlotView(APIView):
    def _get_object(self, id, user_type):
        return TimeSlot.objects.get(id=id, user_type=user_type)

    def _format_time(self, time):
        return str(time.strftime('%c'))

    def get(self, request, iid, cid):
        try:
            interviewer_object = self._get_object(iid, TimeSlot.INTERVIEWER)
            candidate_object = self._get_object(cid, TimeSlot.CANDIDATE)
            common_start_time = max(interviewer_object.available_from, candidate_object.available_from)
            common_end_time = min(interviewer_object.available_to, candidate_object.available_to)

            if common_start_time + timedelta(hours=1) >= common_end_time:
                raise Exception("No common time.")
            time_slots = []
            while (common_start_time + timedelta(hours=1) <= common_end_time):
                time_slots.append({"starting_time": self._format_time(common_start_time),
                                   "ending_time": self._format_time(common_start_time + timedelta(hours=1))})
                common_start_time = common_start_time + timedelta(hours=1)
            return Response(time_slots)
        except TimeSlot.DoesNotExist:
            return Response({"error": "Object does not exist."})
        except Exception as e:
            return Response({"error": str(e)})
