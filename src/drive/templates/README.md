## Agent templates

The kafka topics should adhere to the following naming convention:


### User - Agent:

Consume:
- "agent.<name>.query"
- "agent.master.query"

Produce:
- "agent.<name>.response"
- "agent.master.response"

### Agent - Agent:

- "agent.<producer-name>.<consumer-name>.dispatch"

- "agent.master.searcher.dispatch"
In this case the Searcher agent would be consuming from this topic
and master would be the producer.

- "agent.<consumer-name>.<producer-name>.response"
- "agent.master.searcher.response"
In this case the Master agent would be consuming from this topic,
and listening for response from its initial query.

