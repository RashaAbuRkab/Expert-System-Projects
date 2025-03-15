# Expert System Projects

## --> BuildWise Expert System (Gaza Reconstruction)
This system utilizes fuzzy logic to assess the structural damage of buildings following a conflict and generate recommendations for repair or demolition. It defines linguistic variables (such as foundation condition, stability, and building age), constructs rules, and applies fuzzy reasoning to provide outputs (like "Total Damage" or "Repair Needed").

### Methodology Breakdown:
- Defined input/output variables.
- Created rules for the fuzzy control system.
- Constructed fuzzy reasoning to classify output results.
- Demonstrated system scenarios using forward and backward chaining for different conditions.

### Suggestions for Improvement:
- **Enhancing Rules**: Develop more detailed rules to improve accuracy, especially for buildings with mixed conditions.
- **GUI Development**: A graphical user interface would make the system more user-friendly for non-technical users, such as engineers or disaster response teams.
- **Web or Mobile App**: Deploying the system as an app could provide real-time damage assessments on-site.

## --> System Conflict Scenario for Data Analysts Training
The conflict arises in selecting the best medium for training data analysts. The system presents conflicting rules regarding whether lectures or workshops are more effective for feedback. The proposed solution involves adding an additional variable: "Does it require practical implementation?"

### Suggestions for Handling the Conflict:
- **Enhance Rules**: Consider adding a conditional rule to determine if the training requires practical work, based on the complexity of the topic.
- **Prioritize Practicality**: For topics like Power BI, workshops might be more suitable, while lectures could be better for theoretical concepts such as statistical models.

## --> Fuzzy Logic for System Management (Spares and Utilization)
The fuzzy control system aims to determine the required spare parts based on system metrics like mean delay, server load, and utilization factor. Fuzzy sets have been defined for all variables, and you're now in the process of constructing fuzzy rules.

### Suggestions for Constructing Rules:
- **Example Rule**: If `mean_delay` is "Medium" and `utilisation_factor` is "High", then spares could be "Large." This rule indicates that higher delays and utilization may require larger reserves of spare parts.
- **Refining Rule Set**: Add more specific conditions detailing how `mean_delay` and `utilisation_factor` affect spare part requirements, especially under high usage or significant delays.
