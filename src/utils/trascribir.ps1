# Parametrización de Whisper para ejecutar con opciones predefinidas
param(
    [string]$audio,           # Archivo de audio o múltiples archivos de audio
    [string]$model = "small", # Modelo a utilizar (por defecto "small")
    [string]$output_dir = "./output", # Directorio de salida (por defecto "./output")
    [string]$output_format = "txt",   # Formato de salida (por defecto "txt")
    [bool]$verbose = $true,           # Modo detallado (true o false)
    [string]$task = "transcribe",     # Tarea (por defecto "transcribe")
    [bool]$fp16 = $true               # Uso de precisión FP16 (true o false)
)

# Comando Whisper con los parámetros especificados
whisper $audio `
    --model $model `
    --output_dir $output_dir `
    --output_format $output_format `
    --verbose $verbose `
    --task $task `
    --language es `
    --fp16 $fp16
