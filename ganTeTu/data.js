var dataSource = [
    {
        "id": "Proto-Impl",
        indent: 0,
        "name": "Prototype Implementation",
        "start": new Date(1263715200000),
        "end": new Date(1269183600000),
        "progressValue": 0.42
    },
    {
        "id": "Evaluate-Phase",
        "name": "Evaluate development phase",
        indent: 1,
        "start": new Date(1263715200000),
        "end": new Date(1265650400000),
        "progressValue": 0.1,
        "connectTo": "step1"
    },
    {
        "id": "Evaluate-Tech",
        "name": "Evaluate available technologies",
        indent: 1,
        "start": new Date(1265650400000),
        "end": new Date(1265900400000),
        "progressValue": 0.3
    },
    {
        "id": "Dev-Kit",
        "name": "Choose development kit",
        indent: 1,
        "start": new Date(1265900400000),
        "end": new Date(1266300400000),
        "progressValue": 0.14
    },
    {
        "id": "Proto-Def",
        "name": "Define the Architecture of the Prototype",
        indent: 1,
        "start": new Date(1266300400000),
        "end": new Date(1269183600000),
        "progressValue": 0.68
    },
    {
        "id": "Step1",
        "name": "Step 1: Build prototype",
        indent: 2,
        "start": new Date(1266300400000),
        "end": new Date(1266849600000),
        "progressValue": 0.33,
        "connectTo": "step2"
    },
    {
        "id": "Step2",
        "name": "Step 2: Collect results",
        indent: 2,
        "start": new Date(1266849600000),
        "end": new Date(1267349600000),
        "progressValue": 0.8,
        "connectTo": "step3"
    },
    {
        "id": "Step3",
        "name": "Step 3: Analyze results",
        indent: 2,
        "start": new Date(1267349600000),
        "end": new Date(1267949600000),
        "progressValue": 0.15,
        "connectTo": "follow-up"
    },
    {
        "id": "Follow-up",
        "name": "Follow up with stuff",
        indent: 2,
        "start": new Date(1267949600000),
        "end": new Date(1269183600000),
        "progressValue": 0.74,
        "connectTo": "approval1"
    },
    {
        "id": "Approval1",
        "name": "First customer approval",
        indent: 2,
        "start": new Date(1269194400000)
    },
    {
        "id": "Pre-Planning",
        "name": "Pre-planning",
        "start": new Date(1263715200000),
        "end": new Date(1265450400000),
        indent: 0,
        "progressValue": 0.4
    },
    {
        "id": "Investigate",
        "name": "Investigate the task",
        indent: 1,
        "start": new Date(1263715200000),
        "end": new Date(1264420800000),
        "progressValue": 0.3,
        "connectTo": "distribute"
    },
    {
        "id": "Distribute",
        "name": "Distribute roles and resources",
        indent: 1,
        "start": new Date(1264420800000),
        "end": new Date(1264867200000),
        "progressValue": 0.3,
        "connectTo": "documents"
    },
    {
        "id": "Documents",
        "name": "Gather technical documentation",
        indent: 1,
        "start": new Date(1264867200000),
        "end": new Date(1265450400000),
        "progressValue": 0.65,
    },
    {
        "id": "Planning-Report",
        "name": "Summary planning report",
        indent: 1,
        "parent": "pre-planning",
        "start": new Date(1265550000000)
    },
    {
        "id": "Proto-Impl",
        indent: 0,
        "name": "Prototype Implementation",
        "start": new Date(1263715200000),
        "end": new Date(1269183600000),
        "progressValue": 0.42
    },
    {
        "id": "Evaluate-Phase",
        "name": "Evaluate development phase",
        indent: 1,
        "start": new Date(1263715200000),
        "end": new Date(1265650400000),
        "progressValue": 0.1,
        "connectTo": "step1"
    },
    {
        "id": "Evaluate-Tech",
        "name": "Evaluate available technologies",
        indent: 1,
        "start": new Date(1265650400000),
        "end": new Date(1265900400000),
        "progressValue": 0.3
    },
    {
        "id": "Dev-Kit",
        "name": "Choose development kit",
        indent: 1,
        "start": new Date(1265900400000),
        "end": new Date(1266300400000),
        "progressValue": 0.14
    },
    {
        "id": "Proto-Def",
        "name": "Define the Architecture of the Prototype",
        indent: 1,
        "start": new Date(1266300400000),
        "end": new Date(1269183600000),
        "progressValue": 0.68
    },
    {
        "id": "Step1",
        "name": "Step 1: Build prototype",
        indent: 2,
        "start": new Date(1266300400000),
        "end": new Date(1266849600000),
        "progressValue": 0.33,
        "connectTo": "step2"
    },
    {
        "id": "Step2",
        "name": "Step 2: Collect results",
        indent: 2,
        "start": new Date(1266849600000),
        "end": new Date(1267349600000),
        "progressValue": 0.8,
        "connectTo": "step3"
    },
    {
        "id": "Step3",
        "name": "Step 3: Analyze results",
        indent: 2,
        "start": new Date(1267349600000),
        "end": new Date(1267949600000),
        "progressValue": 0.15,
        "connectTo": "follow-up"
    },
    {
        "id": "Follow-up",
        "name": "Follow up with stuff",
        indent: 2,
        "start": new Date(1267949600000),
        "end": new Date(1269183600000),
        "progressValue": 0.74,
        "connectTo": "approval1"
    },
    {
        "id": "Approval1",
        "name": "First customer approval",
        indent: 2,
        "start": new Date(1269194400000)
    }
];