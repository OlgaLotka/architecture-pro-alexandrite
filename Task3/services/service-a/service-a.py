from flask import Flask, request, jsonify

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor


#tracer
trace.set_tracer_provider(
   TracerProvider(
       resource=Resource.create({SERVICE_NAME: "имя сервиса"})
   )
)
jaeger_exporter = JaegerExporter( #jaeger
   agent_host_name="jaeger",
   agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(
   BatchSpanProcessor(jaeger_exporter) #span creator
)


app = Flask(__name__)
FlaskInstrumentor().instrument_app(app) #flask instrumentation
RequestsInstrumentor().instrument() #request instrumentation 


@app.route('/3d-model', methods=['POST'])
def create_usersScenario():
    with trace.get_tracer(__name__).start_as_current_span("span"):
        data = request.get_json()
        count = data['line-count']
        v = 0 
        for i in range(count):
            for j in range(3):
                v = v + (i*j)
    return jsonify({'volume': v}), 201



if __name__ == '__main__':

    app.run(host="0.0.0.0", port=8084, debug=True)
