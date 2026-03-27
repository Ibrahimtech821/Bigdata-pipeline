data_unprocessed link:https://drive.google.com/file/d/1MW6lzze7AWBtzM4xwrL3XCTfkAeV4eEc/view?usp=drive_link

## Docker

The project includes `pipeline/Dockerfile` with:
- Base image: `python:3.11-slim`
- Installed packages: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `scipy`, `requests`
- Working directory: `/app/pipeline/`
- Default container command: interactive `bash`

### Build

From the project root:

```bash
docker build -f pipeline/Dockerfile -t bigdata-pipeline pipeline
```

### Run

```bash
docker run -it --rm bigdata-pipeline
```
