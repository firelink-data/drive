## Agent templates

Currently only one template agent is available called `master` which job is to take
input from the user and dispatch work to other agents.

## Topic naming convention

The kafka topics should adhere to the following naming conventions:

**Consumer topics**:
- "drive.<sender>.<receiver>.query"
- "drive.<receiver>.<sender>.response"

**Producer topics**:
- "drive.<receiver>.<sender>.response",
- "drive.<sender>.<receiver>.query"

For example with two agents available called `master` and `searcher`, the topic
config could look like:

**Consumer topics**:
- "drive.user.master.query"
- "drive.master.searcher.response"

**Producer topics**:
- "drive.user.master.response"
- "drive.master.searcher.query"

