# Simrunner
Build and runs simulations through bazel

## Entry Point
app/main.py

## Logic
Contacts an api for a sim, then runs the sim.
When done running the sim, checks the api for another sim.
If no sims left, shuts itself off.