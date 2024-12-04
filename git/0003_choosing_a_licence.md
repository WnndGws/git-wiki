# Architectural Decision Record (ADR)

## Title: Adoption of GPLv3 License for Open Source Projects

---

### **Status**: Accepted

### **Context**

The user maintains several GitHub repositories consisting primarily of:

- **Python scripts**
- **Zsh scripts**
- **Documentation**

The user intends to establish a default license for these projects that aligns with their preferences:

- **Maximize Open Source Availability**: Projects should be as open source as possible.
- **Allow Commercial Use**: Others can use the code commercially, provided it remains open source.
- **Permit Copying and Distribution**: Copying and distribution are allowed as long as the code doesn't become closed source.
- **Liability Disclaimer**: The code is provided "as-is," with no liability on the part of the user.

### **Decision**

Adopt the **GNU General Public License version 3 (GPLv3)** as the default license for all repositories.

### **Rationale**

The GPLv3 license aligns with the user's requirements in the following ways:

1. **Strong Copyleft License**

   - **Keeps Code Open Source**: GPLv3 ensures that all copies and derivative works remain open source.
   - **Prevents Proprietary Forks**: Others cannot redistribute the code under a proprietary license.

2. **Allows Commercial Use**

   - **Commercial Flexibility**: Others can use, modify, and distribute the code commercially.
   - **Mandatory Open Sourcing**: Any distributed modifications must also be open source under GPLv3.

3. **Permits Modification and Distribution**

   - **Freedom to Share**: Users can copy and share the code freely.
   - **Consistent Licensing**: Modifications must be licensed under the same terms.

4. **Liability and Warranty Disclaimer**

   - **"As-Is" Provision**: GPLv3 disclaims warranties, aligning with the user's intent.
   - **Limits Liability**: Protects the user from legal claims arising from the use of the code.

### **Alternatives Considered**

1. **MIT License**

   - **Pros**: Simple and permissive; widely used.
   - **Cons**: Allows proprietary derivatives, which conflicts with the user's desire to keep the code open source.

2. **Apache License 2.0**

   - **Pros**: Includes patent protection; allows commercial use.
   - **Cons**: Permissive nature permits closing the source code in derivatives.

3. **GNU Affero General Public License (AGPLv3)**

   - **Pros**: Extends copyleft to network use cases; prevents SaaS loophole.
   - **Cons**: May be unnecessarily restrictive for scripts and documentation not intended for network deployment.

### **Consequences**

- **Positive**

  - **Ensures Open Source Continuity**: All derivatives will remain open source.
  - **Encourages Collaboration**: The license is recognized and respected, fostering community contributions.
  - **Legal Protection**: Liability limitations and warranty disclaimers protect the user.

- **Negative**

  - **License Compatibility**: GPLv3 is not compatible with some other licenses, potentially limiting integration.
  - **Perceived Restrictiveness**: Some developers and companies might avoid GPL-licensed projects due to copyleft obligations.

### **Implementation Plan**

1. **Add a LICENSE File**

   - Include the full text of the GPLv3 license in a `LICENSE` file in each repository.

2. **Update Source File Headers**

   - Add GPLv3 license headers to the top of each source file.

3. **Update Documentation**

   - Clearly state in the README and other documentation that the project is licensed under GPLv3.

4. **Inform Contributors**

   - Establish that all contributions will be licensed under GPLv3 to maintain consistency.

### **Risks and Mitigations**

- **Risk**: Potential contributors may be hesitant due to GPLv3's strong copyleft.
  - **Mitigation**: Provide clear documentation explaining the choice and benefits of GPLv3.
- **Risk**: Incompatibility with other open-source licenses.
  - **Mitigation**: Review dependencies and ensure they are compatible with GPLv3.

---

### **References**

- **GPLv3 License Text**: [https://www.gnu.org/licenses/gpl-3.0.txt](https://www.gnu.org/licenses/gpl-3.0.txt)
- **GNU Licenses Overview**: [https://www.gnu.org/licenses/licenses.en.html](https://www.gnu.org/licenses/licenses.en.html)

---
