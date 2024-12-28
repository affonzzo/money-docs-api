from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from docling.document_converter import DocumentConverter
import uvicorn
from typing import Optional
import io
import os

app = FastAPI(title="Money Docs API")

# Configurar CORS para aceitar requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, substitua por seu domínio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health_check():
    return {"status": "ok", "message": "Money Docs API is running"}

@app.post("/convert")
async def convert_document(
    file: UploadFile,
    output_format: str = Form(...),
    use_ocr: Optional[bool] = Form(False),
    extract_tables: Optional[bool] = Form(True),
    max_pages: Optional[int] = Form(None)
):
    try:
        contents = await file.read()
        file_obj = io.BytesIO(contents)
        
        converter = DocumentConverter()
        result = converter.convert(
            file_obj,
            pipeline_options={
                "do_ocr": use_ocr,
                "do_table_structure": extract_tables,
                "max_num_pages": max_pages
            }
        )
        
        if output_format == "markdown":
            return {"result": result.document.export_to_markdown()}
        elif output_format == "json":
            return {"result": result.document.export_to_dict()}
        elif output_format == "html":
            return {"result": "HTML export not implemented yet"}
        
        return {"error": "Invalid output format"}
        
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)