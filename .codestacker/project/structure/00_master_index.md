# 🧭 Master Documentation Index

This file serves as the **Global Routing Hub** for the Code Stacker Application Architecture.

To prevent separate Workspaces from suffering file-lock conflicts during concurrent "Master Synchronizations," we utilize a **Federated Documentation Model**. 

Instead of writing to a single monolithic file (e.g., `01_project_overview.md`), Workspaces output their major architectural truths into their own dedicated Epic documents inside the `epics/` folder, which are then indexed here.

---

## 🏗️ Core System Foundations

*   **Database Schema:** [02_database_schema.sql](./02_database_schema.sql) *(The only single-source-of-truth file that receives concurrent updates)*
*   **Environment & Ports:** [03_environment.md](./03_environment.md)
*   **File Structure:** [04_file_structure.md](./04_file_structure.md)
*   **Dependencies:** [05_dependencies.md](./05_dependencies.md)
*   **Credentials Protocol:** [06_credentials.md](./06_credentials.md)
*   **Global State Flow:** [07_evolving_state.md](./07_evolving_state.md)

---

## 🗂️ Workspace Epics & Features

*When a Workspace Director completes a major epic, they must link their resulting architectural documentation here.*

### Active Epics:
- *None currently logged.*

### Completed Epics:
- *None currently logged.*
