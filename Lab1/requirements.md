# Peer-to-Peer Carpooling & Expense Splitter
## Software Requirements Specification (SRS) - Lab 1

**Problem Statement:** A commuter ridesharing portal that matches drivers and passengers with overlapping daily routes, enforces detour tolerance thresholds, and calculates automated fuel cost share splits.  
**Key Actors:** Rider Commuter, Driver Host

---

### Requirements Summary Table

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FR-001** | Functional | The system shall calculate route compatibility between driver and passenger commute paths, permitting matches only within a 1.5 km detour tolerance. | High | Given a driver's route and a passenger's pickup/dropoff points, the system returns a match if and only if the total added detour distance for the driver is $\le$ 1.5 km. | Ensures drivers are not inconvenienced by excessive detours while finding compatible passenger routes. |
| **FR-002** | Functional | The system shall calculate automated fuel cost share splits for matched trips based on total distance traveled, vehicle fuel efficiency, and current fuel prices, dividing the cost proportionally among occupants. | High | Upon completion of a shared ride, the system generates an itemized cost split bill showing total trip cost and each participant's exact share within 5 seconds. | Eliminates manual fare calculations and awkward negotiations by providing transparent, automated cost sharing based on objective parameters. |
| **FR-003** | Functional | The system shall allow Driver Hosts and Rider Commuters to set recurring daily commute schedules (e.g., weekday morning/evening pickup times) and query matching commute schedules. | High | Users can define recurring weekly time slots and receive match notifications for overlapping routes within a $\pm$15-minute departure window. | Enables regular daily commuters to establish consistent peer-to-peer carpooling routines without re-entering trip details daily. |
| **FR-004** | Functional | The system shall require Driver Hosts to submit valid driving licenses and vehicle registration documents for verification before publishing ride offers. | High | Unverified driver accounts are prevented from posting ride offers until document verification status is approved by the system or administrator. | Establishes baseline safety, trust, and accountability among peer-to-peer carpool participants. |
| **FR-005** | Functional | The system shall allow a Rider Commuter to send a ride request to a Driver Host for a compatible route and notify both parties upon acceptance or rejection. | Medium | Driver Hosts receive real-time notifications of ride requests and can accept or decline within a 30-minute window, updating seat availability automatically. | Facilitates direct peer-to-peer agreement and prevents overbooking of available vehicle seats. |
| **NFR-001** | Non-Functional | User ratings, driving license verification documents, and travel histories must be stored securely with encrypted backups. | High | Sensitive verification documents and travel logs are encrypted at rest using AES-256 and in transit using TLS 1.3, with automated daily encrypted backups. | Protects personally identifiable information (PII) and legal verification documents from data breaches and unauthorized access in compliance with privacy standards. |
| **NFR-002** | Non-Functional | The system shall compute route matching and detour tolerance calculations for incoming ride search queries within 2 seconds under a concurrent load of up to 1,000 active queries. | High | 95% of route search queries return sorted match results within 2,000 milliseconds during stress testing at peak simulated load. | Ensures a responsive user experience so commuters can quickly evaluate matching rides during peak rush-hour usage. |

---

### Detailed Requirements Breakdown

#### Functional Requirements

##### FR-001: Route Compatibility & Detour Tolerance Matching
* **ID:** FR-001
* **Type:** Functional
* **Description:** The system shall calculate route compatibility between driver and passenger commute paths, permitting matches only within a 1.5 km detour tolerance.
* **Priority:** High
* **Acceptance Criteria:** Given a driver's route and a passenger's pickup/dropoff points, the system returns a match if and only if the total added detour distance for the driver does not exceed 1.5 km.
* **Rationale:** Ensures drivers are not inconvenienced by excessive detours while finding compatible passenger routes.

##### FR-002: Automated Fuel Cost Share Calculation
* **ID:** FR-002
* **Type:** Functional
* **Description:** The system shall calculate automated fuel cost share splits for matched trips based on total distance traveled, vehicle fuel efficiency, and current fuel prices, dividing the cost proportionally among occupants.
* **Priority:** High
* **Acceptance Criteria:** Upon completion of a shared ride, the system generates an itemized cost split bill showing total trip cost and each participant's exact share within 5 seconds.
* **Rationale:** Eliminates manual fare calculations and awkward negotiations by providing transparent, automated cost sharing based on objective parameters.

##### FR-003: Recurring Commute Schedule Matching
* **ID:** FR-003
* **Type:** Functional
* **Description:** The system shall allow Driver Hosts and Rider Commuters to set recurring daily commute schedules (e.g., weekday morning/evening pickup times) and query matching commute schedules.
* **Priority:** High
* **Acceptance Criteria:** Users can define recurring weekly time slots and receive match notifications for overlapping routes within a $\pm$15-minute departure window.
* **Rationale:** Enables regular daily commuters to establish consistent peer-to-peer carpooling routines without re-entering trip details every day.

##### FR-004: Driver Host License & Vehicle Verification
* **ID:** FR-004
* **Type:** Functional
* **Description:** The system shall require Driver Hosts to submit valid driving licenses and vehicle registration documents for verification before publishing ride offers.
* **Priority:** High
* **Acceptance Criteria:** Unverified driver accounts are prevented from posting ride offers until document verification status is approved by the system or administrator.
* **Rationale:** Establishes baseline safety, trust, and accountability among peer-to-peer carpool participants.

##### FR-005: Peer-to-Peer Ride Request & Confirmation Flow
* **ID:** FR-005
* **Type:** Functional
* **Description:** The system shall allow a Rider Commuter to send a ride request to a Driver Host for a compatible route and notify both parties upon acceptance or rejection.
* **Priority:** Medium
* **Acceptance Criteria:** Driver Hosts receive real-time notifications of ride requests and can accept or decline within a 30-minute window, updating seat availability automatically.
* **Rationale:** Facilitates direct peer-to-peer agreement and prevents double booking of available vehicle seats.

---

#### Non-Functional Requirements

##### NFR-001: Data Encryption & Secure Backup Storage
* **ID:** NFR-001
* **Type:** Non-Functional
* **Description:** User ratings, driving license verification documents, and travel histories must be stored securely with encrypted backups.
* **Priority:** High
* **Acceptance Criteria:** Sensitive verification documents and travel logs are encrypted at rest using AES-256 and in transit using TLS 1.3, with automated daily encrypted backups.
* **Rationale:** Protects personally identifiable information (PII) and legal verification documents from data breaches and unauthorized access in compliance with privacy standards.

##### NFR-002: Real-time Route Matching Performance
* **ID:** NFR-002
* **Type:** Non-Functional
* **Description:** The system shall compute route matching and detour tolerance calculations for incoming ride search queries within 2 seconds under a concurrent load of up to 1,000 active queries.
* **Priority:** High
* **Acceptance Criteria:** 95% of route search queries return sorted match results within 2,000 milliseconds during stress testing at peak simulated load.
* **Rationale:** Ensures a responsive user experience so commuters can quickly evaluate matching rides during peak rush-hour usage.
