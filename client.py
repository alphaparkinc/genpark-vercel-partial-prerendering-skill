class NextjsPprSplitterClient:
    def split_page(self, page_structure: dict) -> dict:
        static = [k for k, v in page_structure.items() if v == "static"]
        dynamic = [k for k, v in page_structure.items() if v == "dynamic"]
        return {"static_shell_components": static, "dynamic_suspense_islands": dynamic}