# Workflow

## Ideal

1. - [x] Use Whisper_Streaming to listen for 'RoboRollins', (Replaced with faster_whisper)
2. - [x] Lsiten to the first question after 'RoboRollins',
3. - [ ] Even if the question does not require realtime, activate the token for realtime anyway so we can push the answer through ChatGPT as a response.
4. - [ ] If the question requires realtime token, activate ChatGPT Realtime 4o and enable it for realtime streaming.
5. - [ ] If the question does not require a realtime token, just do a one off question to a simple ChatGPT endpoint and respond through the realtime API.
6. - [x] Wait for no noise or response for at least 30 seconds... cancel the connection. (Set this manually now)

## Questions

1. Can we push a 'fake' response through the realtime API? i.e. We get a response from the ChatGPT 4o as text, we parse that and send it to the ChatGPT Realtime 4o as a Developer or something. (Inject a response) (No we cannot)
2.
