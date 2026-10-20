# Certify

Certify is a Spring Boot application for generating personalized certificates in bulk. It uses a certificate template image and a CSV file containing participant names, creates one PNG certificate for each participant, and packages the results into a ZIP file.

## Project Location

The application source code is in the [`Certify`](./Certify/) directory.

The complete project documentation is available in [`Certify/README.md`](./Certify/README.md).

## Quick Start

Requirements:

- Java Development Kit 21 or later
- A web browser

From the repository root, run:

```powershell
cd Certify
.\mvnw.cmd spring-boot:run
```

Open the application at:

```text
http://localhost:8080/view
```

Upload a certificate template image and a CSV file containing participant names. Select the name position on the template, choose the font size, and generate the certificates. The generated files are saved in `Certify/certificate_output/` and are returned as `certificates.zip`.

## Testing

Run the tests from the repository root:

```powershell
cd Certify
.\mvnw.cmd test
```

For the complete documentation, including project structure, processing flow, CSV format, validation rules, limitations, and future improvements, see [`Certify/README.md`](./Certify/README.md).
