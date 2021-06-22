# Tracing.py

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)

provider = TracerProvider()
processor = SimpleSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

trace = trace.get_tracer(__name__)

with trace.start_as_current_span("foo"):
    with trace.start_as_current_span("bar"):
        with trace.start_as_current_span("baz"):
            print("Hello world from OpenTelemetry Python!")
