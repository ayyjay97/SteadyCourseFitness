# SteadyCourseFitness
Steady Course Fitness is a project for CS 361 at Oregon State University. The program will showcase the use of microservices spread across a group of four different programs.

Built with a modular Microservices Architecture in Python, the application functions as a "system of systems" to provide high-precision athletic tracking and planning. The program is specifically engineered to help users reach defined biometric waypoints and meet rigorous performance benchmarks.

Key Capabilities
Autonomous Goal Mapping: Leverages a specialized "Goal-to-Plan Mapper" service to analyze user biometrics and suggest optimized 15-week workout templates.

Precision Pace Optimization: Features a dedicated calculator that generates exact interval splits for any selectable distance, ensuring users stay on track for their fitness goals.

Decoupled Data Management: Utilizes a "No-Web" inter-process communication (IPC) model where biometric progress and activity logs are managed by independent background services to ensure system integrity and security.

Structured Deliverables: Includes an automated PDF generation engine that transforms raw training data into clean printable rubrics for offline use.