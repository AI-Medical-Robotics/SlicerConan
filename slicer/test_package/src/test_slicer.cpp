#include <vtkSmartPointer.h>
#include <vtkMRMLScene.h>
#include <vtkMRMLNode.h>
#include <gtest/gtest.h>

// Test MRML, Logic, Widgets
// Test VTK, ZMQ

TEST(MRMLCoreTest, CreateNode) {
    // Create a test MRML scene
    vtkSmartPointer<vtkMRMLScene> scene = vtkSmartPointer<vtkMRMLScene>::New();

    // Create a test MRML node
    vtkSmartPointer<vtkMRMLNode> node = vtkSmartPointer<vtkMRMLNode> node = vtkSmartPointer<vtkMRMLNode>::New();
    node->SetName("TestNode");

    // Add the node to the scene
    scene->AddNode(node);

    // Check that the node was added to the scene
    EXPECT_EQ(scene->GetNumberOfNodes(), 1);
    EXPECT_EQ(scene->GetNodeByID(node->GetID()), node);
}


