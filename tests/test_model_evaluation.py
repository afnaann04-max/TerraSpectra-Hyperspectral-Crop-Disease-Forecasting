
import unittest
import numpy as np

from terraspectra.model_evaluation import evaluate_classifier


class TestModelEvaluation(unittest.TestCase):

    def setUp(self):
        self.y_true = np.array([0, 0, 1, 1, 1, 0])
        self.y_pred = np.array([0, 0, 1, 0, 1, 0])

    def test_basic_metrics(self):
        results = evaluate_classifier(self.y_true, self.y_pred)

        self.assertAlmostEqual(results["accuracy"], 5 / 6)
        self.assertIn("balanced_accuracy", results)
        self.assertIn("precision_macro", results)
        self.assertIn("recall_macro", results)
        self.assertIn("f1_macro", results)

    def test_confusion_matrix(self):
        results = evaluate_classifier(self.y_true, self.y_pred)

        self.assertEqual(
            results["confusion_matrix"],
            [[3, 0], [1, 2]]
        )

    def test_weighted_metrics(self):
        results = evaluate_classifier(self.y_true, self.y_pred)

        self.assertIn("precision_weighted", results)
        self.assertIn("recall_weighted", results)
        self.assertIn("f1_weighted", results)

    def test_binary_roc_auc(self):
        probabilities = np.array(
            [0.10, 0.20, 0.80, 0.40, 0.90, 0.30]
        )

        results = evaluate_classifier(
            self.y_true, self.y_pred, probabilities
        )

        self.assertIn("roc_auc", results)
        self.assertGreaterEqual(results["roc_auc"], 0.0)
        self.assertLessEqual(results["roc_auc"], 1.0)

    def test_multiclass_evaluation(self):
        y_true = np.array([0, 1, 2, 0, 1, 2])
        y_pred = np.array([0, 1, 1, 0, 2, 2])

        results = evaluate_classifier(y_true, y_pred)

        self.assertEqual(len(results["class_labels"]), 3)
        self.assertEqual(len(results["confusion_matrix"]), 3)

    def test_mismatched_lengths_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_classifier([0, 1], [0])

    def test_empty_input_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_classifier([], [])

    def test_missing_labels_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_classifier([0, None, 1], [0, 1, 1])

    def test_invalid_probabilities_rejected(self):
        probabilities = np.array([0.2, 1.5, 0.8, 0.4, 0.9, 0.3])

        with self.assertRaises(ValueError):
            evaluate_classifier(
                self.y_true, self.y_pred, probabilities
            )


if __name__ == "__main__":
    unittest.main()
