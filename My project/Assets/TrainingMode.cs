using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TrainingMode : MonoBehaviour
{
    public GameObject BoxPad;
    public float Timer;
    private float BinTimer;
    public Camera camera;

    public void Update()
    {
        BinTimer -= Time.deltaTime;
        if(BinTimer <= 0)
        {
            GameObject var =Instantiate(BoxPad, new Vector3(0, 0, 0), Quaternion.identity);
            Vector3.MoveTowards(var.transform.position, camera.transform.position, 1);
            BinTimer = Timer;
        }
    }
}
