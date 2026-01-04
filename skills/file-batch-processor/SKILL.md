---
name: file-batch-processor
description: This skill should be used when performing batch operations on files such as renaming, converting formats, resizing images, compressing files, or organizing directories. It provides efficient workflows for processing multiple files with consistent operations.
---

# File Batch Processor

Automates batch file operations including renaming, format conversion, resizing, compression, and organization.

## Purpose

Streamlines bulk file processing tasks that would be tedious to perform manually. Provides standardized workflows for common file operations with validation, error handling, and progress tracking.

## When to Use

Use this skill when:
- Renaming multiple files with a pattern
- Converting file formats (images, documents, media)
- Resizing or optimizing images
- Compressing or archiving files
- Organizing files into directories by criteria
- Performing batch metadata operations
- Finding and removing duplicate files

## Usage Guide

### Batch Renaming

To rename files in bulk:

1. Identify the pattern or naming convention
2. Preview the changes before applying
3. Execute the rename operation

Use `scripts/batch_rename.py` with pattern matching and preview mode.

Example: "Rename all JPG files to include today's date"

### Image Processing

To process images:

1. Determine the operation (resize, convert, optimize)
2. Set quality and dimension parameters
3. Process with progress tracking

Use `scripts/image_processor.py` for image operations.

Example: "Convert all PNG files to WebP and resize to 800px width"

### File Organization

To organize files:

1. Define organization criteria (date, type, size, etc.)
2. Create directory structure
3. Move or copy files accordingly

Use `scripts/organize_files.py` to sort files into directories.

Example: "Organize files by creation date into YYYY-MM folders"

### Format Conversion

To convert file formats:

1. Identify source and target formats
2. Configure conversion settings
3. Process files with validation

Reference `references/format-conversions.md` for supported formats and options.

### Duplicate Detection

To find and handle duplicates:

1. Scan directory for files
2. Compare using hash or content
3. Review and remove duplicates

Use `scripts/find_duplicates.py` for duplicate detection.

## Bundled Resources

### Scripts

- `scripts/batch_rename.py` - Pattern-based batch file renaming with preview
- `scripts/image_processor.py` - Batch image operations (resize, convert, optimize)
- `scripts/organize_files.py` - Organize files into directories by criteria
- `scripts/find_duplicates.py` - Find and remove duplicate files
- `scripts/batch_compress.py` - Compress files and create archives

### References

- `references/format-conversions.md` - Supported file format conversions
- `references/naming-patterns.md` - Common file naming patterns and conventions
- `references/image-optimization.md` - Image quality and optimization guidelines

### Assets

- `assets/file-icons/` - Icons for different file types
- `assets/templates/` - Directory structure templates

## Best Practices

1. **Preview First** - Always preview changes before applying
2. **Backup** - Keep backups when performing destructive operations
3. **Validation** - Verify results after batch operations
4. **Logging** - Maintain logs of all operations performed
5. **Error Handling** - Handle errors gracefully without stopping entire batch
