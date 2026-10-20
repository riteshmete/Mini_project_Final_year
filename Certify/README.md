# Certify

Certify is a Spring Boot web application for generating personalized certificates in bulk. It uses an image template and a CSV file containing participant names, places each name at a selected position on the template, generates a PNG certificate for every name, and packages the results into a ZIP archive.

## Features

- Upload a certificate template image.
- Upload a CSV file containing participant names.
- Preview the uploaded template in the browser.
- Select the name position by clicking on the image preview.
- Convert preview coordinates to the original image coordinates automatically.
- Set the certificate name font size.
- Generate one PNG certificate per participant.
- Download all generated certificates as `certificates.zip`.

## Technology Stack

- Java 21
- Spring Boot 4.1.0
- Spring MVC
- Thymeleaf
- HTML, CSS, and plain JavaScript
- Java AWT and ImageIO for image processing
- Maven
- JUnit 5 and Spring Boot test support

## Requirements

Install the following before running the project:

- Java Development Kit (JDK) 21 or later
- A web browser

The project includes the Maven Wrapper, so a separate Maven installation is not required.

## Running the Application

Open a PowerShell terminal in the project root and run:

```powershell
.\mvnw.cmd spring-boot:run
```

After the application starts, open:

```text
http://localhost:8080/view
```

## Using the Application

1. Open the application at `http://localhost:8080/view`.
2. Select a certificate template image.
3. Click the location where the participant name should be placed.
4. Confirm the displayed X and Y coordinates.
5. Select a CSV file containing the participant names.
6. Enter the required font size.
7. Select `Generate Certificates`.
8. Download the generated `certificates.zip` file.

The generated PNG files and ZIP archive are stored in the `certificate_output` directory.

## CSV Format

The first row is treated as a header. The first column of every following non-empty row is used as the participant name.

Example:

```csv
Name
Aarav Sharma
Priya Patil
Rohan Pawar
```

The application generates files similar to:

```text
Aarav_Sharma_Certificate.png
Priya_Patil_Certificate.png
Rohan_Pawar_Certificate.png
```

The current CSV parser uses basic comma splitting. Quoted fields and commas inside a name are not supported.

## Application Endpoints

### `GET /view`

Displays the certificate-generation form.

### `POST /save`

Accepts the multipart form containing:

- The certificate template image
- The CSV file
- The X coordinate
- The Y coordinate
- The font size

The endpoint returns the generated ZIP archive as a file download.

## Project Structure

```text
Certify/
├── pom.xml
├── mvnw
├── mvnw.cmd
├── README.md
├── src/
│   ├── main/
│   │   ├── java/in/ac/project/certify/
│   │   │   ├── CertifyApplication.java
│   │   │   ├── controller/
│   │   │   │   └── CertificateController.java
│   │   │   ├── model/
│   │   │   │   └── CertificateContainer.java
│   │   │   └── service/
│   │   │       └── CertificateService.java
│   │   └── resources/
│   │       ├── application.properties
│   │       ├── static/css/style.css
│   │       └── templates/view_template.html
│   └── test/
│       └── java/in/ac/project/certify/
│           └── CertifyApplicationTests.java
└── certificate_output/
```

## Processing Flow

1. `CertificateController` displays the form at `/view`.
2. The user submits the template, CSV file, coordinates, and font size to `/save`.
3. `CertificateService` validates the submitted values.
4. The service reads participant names from the CSV file.
5. A copy of the template is created for each participant.
6. The participant name is rendered in centered black Arial bold text.
7. Each certificate is saved as a PNG file.
8. The PNG files are added to `certificates.zip`.
9. The ZIP archive is returned to the browser.

## Validation Rules

The application rejects requests when:

- The template image is missing or empty.
- The CSV file is missing or empty.
- The template cannot be read as an image.
- The CSV contains no valid participant names.
- The X or Y coordinate is negative.
- The font size is less than 1 or greater than 200.
- The output directory cannot be created.
- No certificate can be generated.

The maximum configured size for an individual upload and the complete multipart request is 50 MB.

## Running Tests

Run the test suite with:

```powershell
.\mvnw.cmd test
```

The current test suite verifies that the Spring Boot application context loads successfully.

## Building the Application

To create a packaged application, run:

```powershell
.\mvnw.cmd clean package
```

The generated build files are placed in the `target` directory.

## Current Limitations

- Only the first CSV column is used as the participant name.
- CSV parsing does not support quoted fields.
- The font family is fixed to Arial.
- The font color is fixed to black.
- The same coordinates and font size are used for every certificate.
- Generated files are stored on the local file system.
- There is no database or user authentication.
- Error messages are not currently displayed in a dedicated web page.
- Old files in `certificate_output` are not automatically removed.
- The application currently generates PNG certificates only.

## Possible Future Improvements

- Use a dedicated CSV parsing library.
- Support additional certificate fields such as course, date, and grade.
- Allow users to select the font family, color, and alignment.
- Add a certificate preview before generation.
- Add progress reporting for large CSV files.
- Prevent filename conflicts for duplicate participant names.
- Add database storage and certificate history.
- Add authentication and role-based access.
- Support PDF output and email delivery.
- Add service-layer and integration tests for the complete generation workflow.

