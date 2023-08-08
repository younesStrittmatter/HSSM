import hssm

hssm.set_floatX("float32")


def test_non_reg_models(data_ddm):
    model1 = hssm.HSSM(data_ddm)
    model1.sample(cores=1, chains=1, tune=10, draws=10)
    model1.sample(sampler="nuts_numpyro", cores=1, chains=1, tune=10, draws=10)

    model2 = hssm.HSSM(data_ddm, loglik_kind="approx_differentiable")
    model2.sample(cores=1, chains=1, tune=10, draws=10)
    model2.sample(sampler="nuts_numpyro", cores=1, chains=1, tune=10, draws=10)


def test_reg_models(data_ddm_reg):
    param_reg = dict(
        formula="v ~ 1 + x + y",
        prior={
            "Intercept": {"name": "Uniform", "lower": -3.0, "upper": 3.0},
            "x": {"name": "Uniform", "lower": -0.50, "upper": 0.50},
            "y": {"name": "Uniform", "lower": -0.50, "upper": 0.50},
        },
    )

    model1 = hssm.HSSM(data_ddm_reg, v=param_reg)
    model1.sample(cores=1, chains=1, tune=10, draws=10)
    model1.sample(sampler="nuts_numpyro", cores=1, chains=1, tune=10, draws=10)
    model2 = hssm.HSSM(data_ddm_reg, loglik_kind="approx_differentiable", v=param_reg)
    model2.sample(cores=1, chains=1, tune=10, draws=10)
    model2.sample(sampler="nuts_numpyro", cores=1, chains=1, tune=10, draws=10)

    model3 = hssm.HSSM(data_ddm_reg, a=param_reg)
    model3.sample(cores=1, chains=1, tune=10, draws=10)
    model3.sample(sampler="nuts_numpyro", cores=1, chains=1, tune=10, draws=10)

    model4 = hssm.HSSM(data_ddm_reg, loglik_kind="approx_differentiable", a=param_reg)
    model4.sample(cores=1, chains=1, tune=10, draws=10)
    model4.sample(sampler="nuts_numpyro", cores=1, chains=1, tune=10, draws=10)