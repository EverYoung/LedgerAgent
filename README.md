Ledger Agent can scan your bank statements and record all the transactions in the statements in a specific format.

Ledger Agent is built as a multi-agent system using ADK. System structure:

-- Root Agent (Sequential Agent)
   |-- Statement Recorder Agent (Loop Agent)
   |   |-- Statement Parser Agent (LLM Agent)
   |   |-- Statement Review Agent (LLM Agent)
   |-- Format Refiner Agent (LLM Agent)
