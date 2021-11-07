import logging
from .models import Author

logger = logging.getLogger(__name__)

def index(request):
    try:
        news = Author.objects.all()
    except Exception as E:
        print(logger.error(E))