# MediKIT-API-sample-requests
A collection of sample API requests used to demonstrate how to interact with the MediKIT API's

## Usage

1. Clone the repository
2. Install [slumber](https://slumber.lucaspickering.me/)
3. Copy the `.env.example` file to `.env` and fill in the required values
4. Load the environment variables into your shell (either through [direnv](https://direnv.net/) or manually)
5. Run `slumber run` to see the available commands
6. Run `slumber run <command>` to run a specific command

## Environment variables

- `ENV`: The environment to use. Can be `TEST`, `ACC` or `PRD`
- `CLIENT_ID`: The client ID assigned to the application by the MediKIT team
- `SIGNING_KEY_PATH`: The path to the signing key correspoding to the certificate provided to MediKIT used to sign the JWT
- `ORGANIZATION_ID`: The organization ID to use, will be provided by the MediKIT team
- `PATIENT_ID`: The patient ID to use, set so a patient ID does not need to be provided for each request, can be found through the `search-patients` request