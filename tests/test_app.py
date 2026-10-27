import unittest
from app import analyze_openapi
class OpenAPITests(unittest.TestCase):
    def test_generates_operations_and_validation_cases(self):
        spec={"openapi":"3.0.3","info":{"title":"Orders API"},"paths":{"/orders":{"get":{"summary":"List orders","responses":{"200":{"description":"OK"}}},"post":{"requestBody":{},"responses":{"201":{"description":"Created"}}}}}}
        result=analyze_openapi(spec)
        self.assertEqual(result["operation_count"],2)
        self.assertTrue(any(item["kind"]=="validation" for item in result["test_plan"]))
    def test_flags_missing_responses(self):
        result=analyze_openapi({"paths":{"/health":{"get":{}}}})
        self.assertTrue(any("No responses" in item["message"] for item in result["issues"]))
    def test_invalid_spec_rejected(self):
        with self.assertRaises(ValueError): analyze_openapi([])
if __name__=="__main__": unittest.main()
