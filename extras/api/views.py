from extras.filters import JobResultFilterSet, WebhookFilterSet
from extras.models import IXAPI, JobResult, Webhook
from utils.api import ModelViewSet, ReadOnlyModelViewSet, StaticChoicesViewSet

from .serializers import IXAPISerializer, JobResultSerializer, WebhookSerializer


class ExtrasFieldChoicesViewSet(StaticChoicesViewSet):
    fields = [(JobResult, ["status"])]


class IXAPIViewSet(ModelViewSet):
    queryset = IXAPI.objects.all()
    serializer_class = IXAPISerializer


class JobResultViewSet(ReadOnlyModelViewSet):
    queryset = JobResult.objects.all()
    serializer_class = JobResultSerializer
    filterset_class = JobResultFilterSet


class WebhookViewSet(ModelViewSet):
    queryset = Webhook.objects.all()
    serializer_class = WebhookSerializer
    filterset_class = WebhookFilterSet
