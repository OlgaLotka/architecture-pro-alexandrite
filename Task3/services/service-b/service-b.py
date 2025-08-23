from flask import Flask, request, jsonify
import requests

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

url = 'http://localhost:8084/3d-model'
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


@app.route('/order', methods=['POST'])
def create_Order():
    with trace.get_tracer(__name__).start_as_current_span("span"):
        data = request.get_json()
        name = data['name']
        count = data['count']

        headers = {
            'Content-Type': 'application/json'
            }
        body = '{"line-count":8}'

        response = requests.post(url, headers=headers, data=body)
        print("response.content", response.json().get('volume'))

    return jsonify({"name": name, 'volume': response.json().get('volume')}), 201



if __name__ == '__main__':

    app.run(host="0.0.0.0", port=8081, debug=True)
