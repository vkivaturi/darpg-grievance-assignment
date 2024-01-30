import java.io.*;
import hex.genmodel.easy.RowData;
import hex.genmodel.easy.EasyPredictModelWrapper;
import hex.genmodel.easy.prediction.*;
import hex.genmodel.MojoModel;

public class PredictOfficialDRF {
    public static void main(String[] args) throws Exception {
        EasyPredictModelWrapper model = new EasyPredictModelWrapper(
                MojoModel.load("../build/DRF_model_python_1706252040024_1.zip"));

        RowData row = new RowData();
        //row.put("org", "GOVUP");
        row.put("pincode", "203001");

        MultinomialModelPrediction p = model.predictMultinomial(row);
        System.out.println("Label - " + p.label);
        System.out.println("Label index - " + p.labelIndex);
        System.out.println("Label probablity - " + p.classProbabilities[p.labelIndex]);
        System.out.println("Class probabilities: ");
        for (int i = 0; i < p.classProbabilities.length; i++) {
            if (i > 0) {
                System.out.print(",");
            }
            System.out.print(p.classProbabilities[i]);
        }
        System.out.println("");
    }
}